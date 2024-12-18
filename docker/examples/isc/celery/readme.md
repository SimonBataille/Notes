# Python
`pip install celery`
`pip install redis`

# Launch redis docker
`docker run --name redis-container -d -p 6379:6379 redis`

# Test
`celery -A envoi_mails worker --loglevel=info` : worker connect to redis and wait for jobs

## Celery under the hood
Oui, c'est tout à fait ça ! Voici un résumé détaillé de ce qui se passe lorsque vous lancez la commande `celery -A envoi_mails worker --loglevel=info` :

1. **Création du processus worker** :
    - Lorsque vous lancez la commande `celery -A envoi_mails worker --loglevel=info`, Celery démarre un **nouveau processus Python** qui agit comme un **worker**.
    - Ce worker est un processus **indépendant** qui attend des **tâches à exécuter**.

2. **Communication avec le broker (Redis)** :
    - Le worker va se connecter au **broker Redis** (dans votre cas, Redis écoute sur `localhost:6379/0`).
    - Le worker attend alors que des **tâches** lui soient envoyées depuis l'application (via le code qui appelle `apply_async()`, par exemple).
    - Le worker est comme un **serveur** qui est en permanence en écoute pour des **messages (tâches)** venant de l'application via Redis.

3. **Exécution des tâches** :
    - Lorsque vous appelez une tâche, comme `envoi_mail.apply_async(...)`, la tâche est placée dans une **file d'attente** dans Redis.
    - Le worker, qui est en attente, **prend une tâche de la file d'attente**, l'exécute (par exemple, l'envoi d'un mail ou un autre processus asynchrone), puis **indique que la tâche est terminée** (via le backend Redis si vous avez configuré un backend).
    - Si la tâche prend du temps, comme l'envoi d'un e-mail ou l'exécution d'une requête lente, le worker continue à exécuter d'autres tâches de la file d'attente pendant que cette tâche est en cours d'exécution.

4. **Surveillance et logging** :
    - Le **`--loglevel=info`** dans la commande active les logs de Celery, permettant de voir ce qui se passe dans le worker.
    - Vous verrez des messages comme `Task received`, `Task started`, `Task succeeded`, etc., dans la sortie de votre terminal, ce qui vous permet de suivre l'activité des tâches traitées.

### En résumé :

- **Le worker** est un processus Python séparé qui écoute en permanence les messages de Redis pour exécuter des tâches.
- **Le broker Redis** (dans ce cas) est le mécanisme de communication entre votre application et le worker.
- Lorsqu'une tâche est envoyée via `apply_async()`, elle est placée dans la file d'attente Redis.
- Le **worker** prend cette tâche et l'exécute en utilisant Celery.
- Cela permet d'exécuter des tâches asynchrones et parallélisées sans bloquer l'application principale.

### Exemple de Workflow :

1. Vous avez un **script** principal qui appelle une tâche Celery avec `apply_async()` :
    ```python
    envoi_mail.apply_async(args=['destinataire@example.com'])
    ```

2. Un **worker Celery** (créé avec `celery -A envoi_mails worker --loglevel=info`) est en attente et reçoit cette tâche via Redis.

3. Le **worker** exécute la tâche (par exemple, envoie un mail) et, une fois terminée, la tâche est marquée comme terminée et peut être suivie via le backend Redis si configuré.

Ainsi, **les workers Celery sont comme des "serveurs" Python** qui attendent des tâches à exécuter, et ils utilisent Redis pour la gestion des messages entre l'application et les workers.

## Get result
Oui, c'est exactement ça. Dans **Celery**, lorsque le **worker** reçoit une tâche à exécuter, il crée un **processus enfant** (ou un thread selon la configuration de Celery) pour exécuter cette tâche. Une fois la tâche terminée, le **processus enfant** transmet le **résultat au backend**, généralement **Redis** ou **RabbitMQ**, sans passer par une communication directe avec le **worker**. Voici un résumé détaillé du flux :

### 1. **Le processus du Worker dans Celery :**
- Le **worker** est un processus qui attend de nouvelles tâches.
- Lorsqu'une tâche est envoyée à un **worker** (en utilisant `apply_async()` ou via une autre méthode), Celery crée un **processus enfant** pour exécuter la tâche.
- Ce **worker** communique avec **Redis** (ou un autre backend de résultat) pour stocker ou récupérer les résultats des tâches exécutées.

### 2. **Le processus enfant exécute la tâche :**
- **Le processus enfant** exécute le code de la tâche en question.
- Dès que la tâche est terminée, le processus enfant **place directement** le résultat dans le backend **Redis**, sous une clé spécifique à la tâche (généralement le `task_id`).
- Le processus enfant n'a pas besoin de communiquer avec le **worker** pour l'envoi du résultat, car ce dernier est géré de manière asynchrone via le backend.

### 3. **Le backend Redis :**
- **Redis** (ou le backend configuré) agit comme un **store centralisé** pour stocker le résultat des tâches.
- Le worker, ou un autre client, peut ensuite utiliser l'**`task_id`** pour récupérer les résultats de la tâche depuis le backend.
- Le backend est souvent configuré pour être utilisé comme une **file d'attente de résultats**. Le worker interroge ce backend à intervalles réguliers ou via une méthode bloquante (`get()`) pour obtenir les résultats des tâches exécutées.

### 4. **Récupération du résultat :**
- Lorsque le worker souhaite récupérer le résultat, il **interroge Redis** à l'aide du `task_id` de la tâche qu'il a envoyée.
- Le worker récupère alors le **résultat** du backend (Redis, par exemple) avec la méthode **`result.get()`** ou en utilisant des mécanismes similaires.

### 5. **Communication indépendante :**
- **Le processus parent (worker)** et le **processus enfant** ne partagent pas directement de mémoire. Ils communiquent plutôt via un **backend de résultats**, comme **Redis**, qui fait office de **mémoire intermédiaire** pour stocker les résultats des tâches.
- Une fois la tâche exécutée, le résultat est mis dans Redis, et le worker peut le récupérer en utilisant l'ID de la tâche.

### Exemple de workflow :
1. Le **client** envoie une tâche à **Celery** (par exemple, `add.delay(2, 3)`).
2. Le **worker** reçoit la tâche et lance un **processus enfant** pour exécuter la tâche.
3. Le **processus enfant** effectue le calcul, par exemple `5`, et place le résultat dans **Redis**.
4. Le **worker** interroge **Redis** pour récupérer le résultat de la tâche en utilisant `result.get()`.

### Conclusion :
Le worker **n'a pas besoin** d'attendre directement la fin du processus enfant pour récupérer le résultat. Le résultat est mis dans un backend partagé comme **Redis**, et c'est ce backend qui fait le lien entre les processus en utilisant un identifiant unique de la tâche (`task_id`). Ce mécanisme permet une gestion asynchrone des tâches dans Celery et offre une séparation claire des responsabilités entre le worker et les processus enfants.


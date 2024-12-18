# Python : install fastapi
- `pip install fastapi`
- `pip install pydantic`
- `pip install uvicorn`

- `uvicorn main:app`
- `http://localhost:8000/docs` : doc swagger swaggerUi integrated in fastapi
- `http://127.0.0.1:8000/openapi.json` : doc openApi format json

- Le fichier openapi.json est généré dynamiquement dans la mémoire (le heap du processus Python) du serveur FastAPI lorsque tu fais une requête vers l'URL /openapi.json

# fichier json
Le fichier JSON qui décrit l'API dans FastAPI (et qui est utilisé par Swagger) est généré dynamiquement au moment où tu accèdes à l'URL /openapi.json pendant que le serveur FastAPI fonctionne. Ce fichier n'est pas stocké sur le disque ou dans un fichier statique dans l'application, mais est généré à la volée en fonction de la structure de ton API, de tes modèles Pydantic, et des routes définies.
## Explication détaillée :

1. Stockage dans le navigateur :
- Lorsque tu accèdes à l'URL http://127.0.0.1:8000/openapi.json dans un navigateur, le fichier JSON est généré dynamiquement par FastAPI et envoyé au navigateur comme une réponse HTTP.
- Le fichier JSON lui-même n'est pas stocké dans le navigateur à moins que tu ne choisisses de le télécharger manuellement (par exemple en cliquant droit > "Enregistrer sous" dans le navigateur).

2. Stockage dans la mémoire du serveur :
- Le fichier openapi.json est effectivement généré dans la mémoire du serveur FastAPI, c'est-à-dire dans le processus Python qui exécute l'application FastAPI. Lorsque tu accèdes à l'URL /openapi.json, FastAPI crée et envoie ce fichier en réponse à la requête, basé sur les informations sur les routes, les modèles, et les configurations de l'API définies dans le code Python.
- Il n'est pas stocké en tant que fichier physique sur le disque du serveur, mais est calculé en temps réel chaque fois qu'une requête est effectuée pour l'URL /openapi.json.

3. Durée de vie du fichier JSON :
- Le fichier JSON est généré à la volée pendant que le serveur est en fonctionnement, et sa durée de vie est limité au temps de fonctionnement du serveur. Dès que le serveur FastAPI s'arrête ou redémarre, le fichier JSON sera généré à nouveau lors de la prochaine requête pour /openapi.json.

## Exemple de flux :

1. Tu démarres ton serveur FastAPI.
2. Lorsque tu accèdes à http://127.0.0.1:8000/docs, Swagger UI affiche l'interface graphique de la documentation de ton API.
3. Swagger UI interroge automatiquement http://127.0.0.1:8000/openapi.json pour obtenir la description de l'API en format JSON.
4. FastAPI génère alors en temps réel ce fichier JSON, qui est envoyé au navigateur et utilisé pour afficher la documentation.

## Résumé :

Le fichier openapi.json n'est pas stocké physiquement dans ton projet ou sur le disque, il est généré dynamiquement à partir des métadonnées de ton application FastAPI. Si tu veux le sauvegarder, tu peux le télécharger manuellement depuis l'URL /openapi.json ou utiliser des outils pour l'enregistrer.

# Async
Oui, l'API de la base de données est indirectement au courant de l'état de la tâche dans l'event loop, mais pas directement via un "identifiant" de tâche comme on pourrait le concevoir dans des systèmes de gestion de tâches. Voici comment cela fonctionne :

### 1. L'API asynchrone et l'event loop
Dans un environnement asynchrone comme celui de `asyncio` en Python, lorsqu'une fonction asynchrone (par exemple, une requête à la base de données) est appelée avec `await`, l'event loop prend en charge la gestion de cette tâche. L'API de la base de données n'a pas besoin de connaître spécifiquement l'ID de la tâche, car elle travaille avec le mécanisme de gestion des événements d'`asyncio` (ou d'autres bibliothèques asynchrones comme `asyncpg` ou `aiomysql`).

### 2. Comment le mécanisme fonctionne-t-il sous le capot ?

Voici une explication étape par étape du processus de gestion d'une requête asynchrone :

#### a) Création de la tâche dans l'event loop :
Lorsqu'une fonction comme `await conn.fetch('SELECT * FROM my_table')` est appelée, l'event loop crée une tâche asynchrone. Cette tâche représente la requête en attente.

#### b) Mise en pause de la tâche :
Dès que l'appel à la base de données est effectué, la tâche est mise en pause, et l'event loop est libre de traiter d'autres tâches en attendant que la réponse de la base de données arrive. À ce moment, la base de données n'a aucune connaissance directe de l'event loop ni de l'ID de la tâche. Elle est simplement informée que la requête a été envoyée et attendra une réponse.

#### c) Réponse de la base de données :
Lorsque la base de données répond (en général, via un événement ou une callback), la bibliothèque cliente (par exemple, `asyncpg` ou `aiomysql`) réveille la tâche qui a été mise en pause. C'est-à-dire qu'elle indique à l'event loop que la tâche peut reprendre son exécution. Le code dans la fonction asynchrone continue là où il a été suspendu, avec la donnée ou la réponse obtenue de la base de données.

La bibliothèque cliente, qui gère la communication avec la base de données, connaît en quelque sorte le **contexte de la tâche** en cours, mais elle n'a pas besoin de gérer explicitement un "ID" de la tâche dans l'event loop. Elle sait simplement que lorsque la réponse est prête, elle peut reprendre l'exécution de cette tâche.

#### d) La gestion des événements et des tâches :
En résumé, la base de données n'a pas besoin de gérer explicitement un identifiant pour chaque tâche dans l'event loop. Elle répond à l'événement d'une requête spécifique, et l'event loop permet à la tâche de reprendre son exécution en fonction de cet événement. Cela repose sur un mécanisme de notification d'événements : une fois que l'événement (la réponse de la base de données) se produit, l'event loop reprend la tâche correspondante.

### 3. La bibliothèque cliente et l'event loop :
Les bibliothèques clientes (comme `asyncpg`, `aiomysql`, etc.) sont conçues pour intégrer parfaitement la gestion des événements dans l'event loop. Elles ne nécessitent pas de connaissance explicite du thread ou de l'ID de la tâche en cours. Elles attendent simplement la fin d'une opération (comme la réponse de la base de données) et réactivent la tâche correspondante en appelant des mécanismes internes de l'event loop.

### Exemple pour illustrer :

```python
import asyncio
import asyncpg

async def get_data():
    conn = await asyncpg.connect('postgresql://user:password@localhost/mydatabase')
    result = await conn.fetch('SELECT * FROM my_table')  # Tâche mise en pause ici
    print(result)  # Reprend l'exécution une fois la réponse reçue
    await conn.close()

# Lancer l'event loop
asyncio.run(get_data())
```

Dans cet exemple :

- L'appel à await conn.fetch(...) met la tâche en pause, ce qui signifie que l'event loop peut continuer à traiter d'autres tâches pendant que l'attente de la réponse est en cours.
- L'API de la base de données (ici asyncpg) envoie la requête, mais elle n'a pas besoin de gérer explicitement un ID de tâche ou un objet de tâche dans l'event loop.
- Une fois la réponse reçue, asyncpg réactive la tâche dans l'event loop pour que l'exécution reprenne (affichage des résultats et fermeture de la connexion).

### 4. Conclusion :

- L'API de la base de données ne connaît pas l'ID de la tâche dans l'event loop, mais elle est intégrée avec le mécanisme d'événements de l'event loop.
- L'event loop s'occupe de la gestion des tâches, en mettant en pause celles qui attendent des événements externes et en les reprenant une fois que ces événements sont reçus.
- Les tâches ne sont pas gérées directement par la base de données ; ce sont les bibliothèques clientes (comme asyncpg ou aiomysql) qui assurent la communication avec la base de données et la réactivation des tâches lorsque la réponse est prête.

En résumé, l'event loop et l'API de la base de données sont étroitement intégrés, mais l'API de la base de données ne nécessite pas de connaissance explicite des tâches en cours dans l'event loop. Elle se contente de répondre aux événements, et l'event loop reprend la tâche en conséquence.

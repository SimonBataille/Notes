
# Appels des bibliothèques dynamiques (.so) sous Linux

Lorsqu’un processus Linux appelle une bibliothèque dynamique (.so), **l’OS ne crée pas un nouveau processus** pour exécuter le .so. Voici une explication détaillée de son fonctionnement :

---

## 1. Chargement des bibliothèques dynamiques (.so)
- Les bibliothèques dynamiques (.so, shared objects) contiennent du code compilé qui peut être utilisé par plusieurs processus.
- Lorsqu’un programme exécutable utilise une bibliothèque .so :
  - **Le chargeur dynamique (`ld.so`)** charge le code de la bibliothèque dans l'espace mémoire du processus appelant.
  - Le code de la bibliothèque devient **une partie du processus appelant**, et non un processus séparé.
  - Le processus utilise directement les fonctions et ressources de la bibliothèque.

---

## 2. Aucune création de nouveau processus
- Le code de la bibliothèque .so est exécuté dans le **même processus** que le programme qui l'appelle.
- Il n’y a pas besoin de communication entre processus, car tout se passe dans un seul espace mémoire.

---

## 3. Partage de mémoire RAM
- Le partage de mémoire intervient lorsque plusieurs processus utilisent la même bibliothèque .so.
- Dans ce cas, le système d’exploitation charge le code de la bibliothèque dans une **zone de mémoire partagée** (appelée **text segment**), accessible en lecture seule à tous les processus.
- Cela permet de réduire l’utilisation de la mémoire :
  - **Le code est partagé**, mais chaque processus dispose de sa propre copie des **données globales** ou des **variables locales** (dans le segment data ou heap).

---

## 4. Communication entre le processus et la bibliothèque
- Il n’y a pas d’échange explicite de données entre le processus et la bibliothèque comme avec des mécanismes d’IPC (pipes, mémoire partagée, etc.).
- Le processus appelle directement les fonctions de la bibliothèque via des **pointeurs de fonction** ou des appels dynamiques résolus par le chargeur dynamique.

---

## Résumé simplifié

| **Concept**                | **Réel fonctionnement**                                                                 |
|----------------------------|----------------------------------------------------------------------------------------|
| Création de nouveau processus pour .so ? | **Non** : La bibliothèque est exécutée dans le même processus que l'appelant.         |
| Partage de mémoire RAM ?    | **Oui** : Le code de la bibliothèque est chargé en mémoire partagée pour être utilisé par plusieurs processus. |
| Échange de données ?        | **Directement dans le même espace mémoire** via des appels de fonction.                |

---

Si vous avez d'autres questions sur le fonctionnement des bibliothèques dynamiques ou des processus sous Linux, n'hésitez pas !

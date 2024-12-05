# Différence entre le binaire `tesseract` et la bibliothèque partagée `tesseract.so`

## 1. **Tesseract (binaire exécutable)** :
- Le **binaire `tesseract`** est un programme complet qui inclut non seulement les bibliothèques nécessaires pour exécuter l'OCR, mais également toute la logique de gestion des entrées et sorties, le traitement des images, le modèle de langage, et d'autres fonctionnalités.
- Ce binaire contient donc tout ce qui est nécessaire pour fonctionner de manière autonome, sans dépendre d'autres processus externes pour son fonctionnement, hormis la bibliothèque standard et les dépendances système nécessaires.
- Il peut être "plus lourd" en termes de taille sur le disque, car il inclut non seulement les bibliothèques, mais aussi des outils internes et des ressources comme les modèles de langue, les dictionnaires, etc.

## 2. **Tesseract.so (bibliothèque partagée)** :
- Une **bibliothèque partagée** (`.so` pour Shared Object) est une unité de code qui peut être utilisée par d'autres programmes (comme `pytesseract` par exemple) pour accéder à des fonctionnalités sans avoir à inclure tout le code dans le programme principal.
- Elle ne contient que les fonctionnalités spécifiques pour effectuer certaines tâches (par exemple, des fonctions de traitement d'image, ou des opérations d'OCR), mais pas de logique autonome pour gérer l'entrée ou la sortie des données. Le programme principal (ici, `tesseract` ou un autre wrapper) doit être responsable de l'appel aux fonctions de la bibliothèque et de la gestion des données.
- Le fichier `.so` est généralement plus petit que le binaire complet, car il ne contient que le code nécessaire pour l'exécution des fonctions spécifiques, et non le programme complet avec sa gestion des entrées/sorties.

## Pourquoi le binaire est "plus lourd" :
- **Autonomie** : Le binaire `tesseract` est un programme autonome, qui peut être exécuté indépendamment, avec toutes les ressources (dépendances et bibliothèques) embarquées dans le fichier exécutable ou référencées via des fichiers de configuration. Cela en fait un fichier plus volumineux.
- **Modèles et ressources supplémentaires** : Le binaire `tesseract` inclut généralement des **modèles de langue** (comme `eng.traineddata` pour l'anglais), des **fichiers de configuration**, des outils internes, et d'autres ressources nécessaires pour réaliser les différentes étapes de l'OCR (prétraitement d'image, découpage, reconnaissance, etc.).
- **Implémentation des bibliothèques** : En revanche, la bibliothèque partagée `.so` est uniquement utilisée par des applications externes pour **accéder aux fonctions de traitement d'image** et de reconnaissance de texte. Cela signifie qu'elle ne contient que le code de ces fonctions spécifiques, et n'inclut pas la gestion des fichiers ou des ressources externes.

## En résumé :
- **Tesseract (binaire)** : Un programme complet et autonome pour effectuer l'OCR, plus "lourd" car il inclut tout ce qu'il faut pour fonctionner de manière indépendante (y compris les bibliothèques et ressources).
- **Tesseract.so (bibliothèque partagée)** : Un fichier contenant uniquement le code de la fonction OCR, plus léger, et utilisé dans le cadre d'autres programmes (comme `pytesseract`) qui interagissent avec ce code via des appels de fonctions spécifiques.

En conclusion, **Tesseract** en tant que binaire inclut plus de fonctionnalités et d'éléments (ressources, gestion de l'exécution, etc.) que la bibliothèque `.so`, ce qui le rend plus volumineux.


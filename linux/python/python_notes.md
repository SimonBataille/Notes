# Notes about python on linux system

## Where are packages installed ?

```
>>> help('modules')
/lib/site-packages in your Python folder

>>> import module_name
>>> print(module_name.__file__)
>>> import pygal
>>> print(pygal.__file__)

>>> import os
>>> print(os.__file__)
/usr/lib/python3.8/os.py
```


```
>>> dir(math)
>>> help(math)
>>> help('_sha1')
```

## Python packages links
- https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
- https://www.tutorialsteacher.com/python/python-package

## Packages nécessaires pour python en global
1. To create venv
```
sudo apt install python3.11-venv
sudo apt install python3-pip
sudo apt install python3-pandas python3-matplotlib
```
2. header `python.h` pour les structures compréhensibles par python et retournées par lib en c comme numpy
```
sudo apt install python3-dev : header python.h pour les structures compréhensibles par python et retournées par lib en c comme numpy 
```
3. library for postgresql 
```
sudo apt install libpq-dev : header files for libpq5 (PostgreSQL library)
```
- Le paquet libpq-dev est essentiel pour le développement d'applications qui interagissent avec PostgreSQL, car il contient les fichiers d'en-tête (headers) nécessaires à l'utilisation de la bibliothèque libpq, qui est la bibliothèque C pour l'interface client de PostgreSQL.
- libpq est la bibliothèque cliente de PostgreSQL qui permet aux applications de se connecter à une base de données PostgreSQL, d'exécuter des requêtes SQL et de récupérer des résultats

## venv vs global
1. utile d'avoir certains package en global => installation avec apt install python3-xxx
- certains packages ne sont installables que dans des venv

2. error: externally-managed-environment

- Reason behind the 'Externally Managed Environment' Error

- Ubuntu 23.04, Fedora 38 and probably other recent distribution versions are implementing this enhancement on the use of Python packages.

- The change has been done to avoid the "conflict between OS package managers and Python-specific package management tools like pip. These conflicts include both Python-level API incompatibilities and conflicts over file ownership.

- https://peps.python.org/pep-0668/

## Links between C and Python : python.h
- Lorsqu'un programme Python fait import numpy, c'est l'interpréteur Python qui gère le chargement des fonctions compilées en C. Ensuite, lorsque tu utilises des fonctions comme np.dot(), Python appelle des fonctions C compilées qui sont exécutées par l'ordinateur, tout en utilisant des mécanismes de liaison entre Python et C (comme Python.h) pour gérer les arguments, les résultats, et les exceptions.

- L'interpréteur Python oriente l'exécution du code, mais les calculs eux-mêmes, dans le cas de NumPy, sont réalisés par du code C compilé, ce qui explique la rapidité et l'efficacité de la bibliothèque.

- En résumé, Python est un programme compilé en C (via CPython), capable d'exécuter des modules ou des bibliothèques en C en les appelant dynamiquement lors de l'exécution. Cela permet à Python d'allier sa simplicité de syntaxe à la puissance et à la vitesse d'exécution du code natif compilé en C, ce qui est particulièrement utile pour des bibliothèques comme NumPy, pandas, ou SciPy, qui font des calculs lourds à très grande vitesse.

- Quand numpy est appelée elle retoure le résultat sous-forme de structure compréhensible par python. Elle trouve ces structures dans le fichiers ```python.h.```

  ### Running flow of c-library calls
- Exemple du flux d'exécution complet

1. Prenons un exemple simple de ce processus :

    - Appel d'une fonction Python :

    ```
    result = np.dot([1, 2], [3, 4])
    ```

2. Fonction C exécutée :

    - NumPy effectue le calcul du produit scalaire en C, qui est très rapide.

3. Retour du résultat à Python :

    - Une fois que le résultat (par exemple, un entier 11) est calculé en C, NumPy utilise une fonction comme PyLong_FromLong(11) pour créer un objet Python représentant cet entier.

4. Interpréteur Python :

    - Python récupère cet objet entier et peut maintenant l'utiliser dans le reste du programme Python.

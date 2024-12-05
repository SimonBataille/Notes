# Notes about python on linux system

## A. Where are packages installed ?

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

## B. Python packages/modules
### B.1. Links
- https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
- https://www.tutorialsteacher.com/python/python-package

### B.2. Modules, Packages
- globalement installés dans /usr/lib/python3/dist-packages/
- Module = fichier
- Package = plusieurs fichiers organisés avec __init.py__


### B.3. Package 
- L'instruction __all__ dans un fichier Python est une liste spéciale qui définit les noms des objets (fonctions, classes, variables, etc.) qui seront exportés lorsque le module est importé avec l'instruction from <module> import *.

- Ce qui se passe quand tu fais import pandas :

    Le fichier __init__.py est exécuté.
    Grâce aux importations dans __init__.py, les éléments principaux comme DataFrame, Series, et d'autres fonctions de base sont rendus disponibles directement dans l'espace de noms pandas.
    Cela signifie que, même si les définitions des fonctions et classes sont réparties dans différents modules (core, io, plotting, etc.), tu peux y accéder via pandas.DataFrame, pandas.read_csv, etc. sans avoir besoin d'importer chaque sous-module individuellement


### B.4. Importation vs exécution
```
if __name__ == "__main__":
    main()

"""module_test.py
def main():
    print("Le fichier est exécuté directement")

if __name__ == "__main__":
    main()
"""
```

- python module_test.py => Le fichier est exécuté directement, Dans ce cas, __name__ vaut "__main__", donc la fonction main() est appelée.

- import module_test => Dans ce cas, __name__ dans module_test.py ne sera pas "__main__", mais "module_test". Par conséquent, la fonction main() ne sera pas appelée et rien ne sera imprimé automatiquement.


### B.5. Import
```
from numpy import * => permet de ne pas taper np.module à chaque fois, just module
```

## C. Packages nécessaires pour python en global
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

## D. venv vs global
1. utile d'avoir certains package en global => installation avec apt install python3-xxx
- certains packages ne sont installables que dans des venv

2. error: externally-managed-environment

- Reason behind the 'Externally Managed Environment' Error

- Ubuntu 23.04, Fedora 38 and probably other recent distribution versions are implementing this enhancement on the use of Python packages.

- The change has been done to avoid the "conflict between OS package managers and Python-specific package management tools like pip. These conflicts include both Python-level API incompatibilities and conflicts over file ownership.

- https://peps.python.org/pep-0668/

## E. Links between C and Python : python.h
### E.1. C-library call

    - Lorsqu'un programme Python fait import numpy, c'est l'interpréteur Python qui gère le chargement des fonctions compilées en C. Ensuite, lorsque tu utilises des fonctions comme np.dot(), Python appelle des fonctions C compilées qui sont exécutées par l'ordinateur, tout en utilisant des mécanismes de liaison entre Python et C (comme Python.h) pour gérer les arguments, les résultats, et les exceptions.

    - L'interpréteur Python oriente l'exécution du code, mais les calculs eux-mêmes, dans le cas de NumPy, sont réalisés par du code C compilé, ce qui explique la rapidité et l'efficacité de la bibliothèque.

    - En résumé, Python est un programme compilé en C (via CPython), capable d'exécuter des modules ou des bibliothèques en C en les appelant dynamiquement lors de l'exécution. Cela permet à Python d'allier sa simplicité de syntaxe à la puissance et à la vitesse d'exécution du code natif compilé en C, ce qui est particulièrement utile pour des bibliothèques comme NumPy, pandas, ou SciPy, qui font des calculs lourds à très grande vitesse.

    - Quand numpy est appelée elle retoure le résultat sous-forme de structure compréhensible par python. Elle trouve ces structures dans le fichiers ```python.h.```

### E.2. Running flow of c-library calls
0. Exemple du flux d'exécution complet

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

## F. Syntax
### F.1. Dictionnaires, list
```
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]

nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}
```


### F.2. pytest, mock
```
def test_afficher_liste(mocker):
    mocker.patch('builtins.input', return_value="1,3,5,6") => on mocke la fonction input pour faire comme si on rentrait 1,2,3,4
    captured_output = StringIO()
    sys.stdout = captured_output => on redirige stdout vers le stringIO (rien ne sera vu sur la console)
    main.main() => on execute le main
    output = captured_output.getvalue() => le retour de main est stocké dans output
    sys.stdout = sys.__stdout__ => on remet le retour dans la console 
    expected_value = "['1', '3', '5', '6']"
    assert expected_value in output => on vérifie que output contient les values attedues
```

## G. pyenv
### G.0. Résumé
- Le système peut gérer une seule version de Python par défaut.
- Pyenv permet de gérer plusieurs versions de Python et d'utiliser des environnements virtuels pour les projets.
- Utiliser Pyenv et ses environnements virtuels permet d'assurer une isolation complète des dépendances et des versions, ce qui est crucial pour le développement de projets en Python.

### G.1.Résumé :
- Pyenv modifie les symlinks pour pip dans le répertoire ~/.pyenv/shims, de la même manière qu'il le fait pour python.
- Chaque version de Python installée avec Pyenv a son propre pip, et Pyenv gère les symlinks pour que tu utilises toujours le bon pip pour la version de Python que tu as choisie.
- Cela permet une gestion cohérente des packages Python à travers différentes versions, tout en gardant l'environnement global du système intact.

### G.2. Dépendance de pyenv virtualenv sur python3.11-venv

1. Installation de Python via Pyenv :
- Lorsque tu exécutes pyenv install 3.11.0, Pyenv télécharge et compile la version 3.11.0 de Python, et cette installation comprend toutes les fonctionnalités standard de Python, y compris le module venv, qui est utilisé pour créer des environnements virtuels.
- Les fichiers de cette version de Python sont installés dans ~/.pyenv/versions/3.11.0/.

2. Création d’un Environnement Virtuel :
- Lorsque tu utilises la commande pyenv virtualenv 3.11.0 mon_projet, Pyenv s’appuie sur la version de Python que tu as installée (dans ce cas, 3.11.0).
- Pyenv utilise le module venv de Python pour créer l'environnement virtuel, ce qui signifie que la création de l'environnement virtuel dépend de la version de Python que tu as installée avec Pyenv.

3. Pas de Dépendance Externe :
- Il n’est pas nécessaire d’installer un package distinct tel que python3.11-venv via le gestionnaire de paquets de ton système, car la version de Python que tu installes avec Pyenv contient déjà le module venv.
- Pyenv gère tout cela en interne, et tu n'as pas à te soucier de conflits avec les installations de Python du système.

## H. Anaconda
### H.1. Anaconda on linux
Tout est géré par projet dans ~/anaconda 
```
conda create -n mon_env python=3.x
conda activate mon_env
conda deactivate
```
### H.2. Update bashrc
```
bashrc
alias load_pyenv='export PATH="$HOME/.pyenv/bin:$PATH" && eval "$(pyenv init --path)" && eval "$(pyenv init -)"'
alias load_conda='export PATH="$HOME/anaconda3/bin:$PATH"'
```

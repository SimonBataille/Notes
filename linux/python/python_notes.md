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

# Links
- https://huggingface.co/TheBloke/Llama-2-7B-GGUF
- https://medium.com/@fradin.antoine17/3-ways-to-set-up-llama-2-locally-on-cpu-part-1-5168d50795ac
- conda install conda-forge::llama-cpp-python

# llama.cpp

1. llama.cpp ?

- llama.cpp est une bibliothèque open-source conçue pour exécuter les modèles de langage LLaMA (Large Language Model Meta AI) sur des systèmes locaux, en particulier ceux équipés de ressources limitées (comme des processeurs sans GPU ou des environnements avec des contraintes de mémoire). L'objectif principal de llama.cpp est de permettre l'exécution des modèles LLaMA sur des machines locales en optimisant les performances tout en rendant les modèles plus accessibles.

2. Installation de llama.cpp via Conda

- llama.cpp est automatiquement compilé et intégré dans la bibliothèque Python llama-cpp-python.
- Conda installe cette bibliothèque compilée dans l'environnement Conda actif.
- La version compilée de llama.cpp est incluse comme une dépendance dans llama-cpp-python. Elle est stockée sous forme d'une bibliothèque partagée native, comme un fichier .so (Linux), .dylib (macOS), ou .dll (Windows).
 
3. Where is llama installed

- Chemin : `<chemin-vers-conda>/envs/my_env/lib/pythonX.X/site-packages/llama_cpp/`
- Fichier : `llama_cpp.cpython-<version>.so`

```python
import llama_cpp
import os

print(llama_cpp.__file__)  # Chemin vers le fichier principal du package
```

3. Comment llama-cpp-python utilise-t-il llama.cpp ?

- Le package `llama-cpp-python` est un wrapper Python pour `llama.cpp`.
- Lors de l'installation, le code C++ de llama.cpp est compilé automatiquement en une bibliothèque partagée compatible avec Python, qui est ensuite placée dans le répertoire site-packages.

4. Exemple de fichier dans l'installation

- Une fois installé, le répertoire llama_cpp peut contenir les fichiers suivants :

```
Fichier compilé C++ : llama_cpp.cpython-<version>.so (ou .dll sous Windows).
Fichiers Python :
    __init__.py : Initialise le module Python.
    llama_cpp.py : Contient les bindings Python.
```

5. En résumé

- Lorsque vous installez llama-cpp-python avec conda :

    Le package est installé dans le répertoire de l’environnement Conda activé, sous lib/pythonX.X/site-packages/llama_cpp/.
    Vous pouvez localiser son chemin exact en utilisant soit conda list, soit en imprimant llama_cpp.__file__ dans un script Python.

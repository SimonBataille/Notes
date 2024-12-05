'''
conda install conda-forge::tesseract
~sudo apt install tesseract-ocr
conda install conda-forge::pytesseract
~pip install pytesseract
conda list pytesseract
conda list tesseract
which tesseract
'''

import pytesseract
from PIL import Image

# Assurez-vous que tesseract est bien installé et accessible
print("Vérification de tesseract version:")
try:
    tesseract_version = pytesseract.get_tesseract_version()
    print(f"Tesseract Version: {tesseract_version}")
except Exception as e:
    print(f"Erreur: Impossible de récupérer la version de tesseract. Détails: {e}")

# Spécifier le chemin vers l'exécutable tesseract si nécessaire
# Si tesseract n'est pas dans le PATH global, spécifiez le chemin absolu du binaire
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
# Exemple: pytesseract.pytesseract.tesseract_cmd = '/chemin/vers/tesseract'
# teeseract est un binaire autonome contrairement a tesseract.so
pytesseract.pytesseract.tesseract_cmd = '/home/simon/anaconda3/envs/isc_environment/bin/tesseract'

# Charger une image de test (remplacez ce chemin par une image valide)
image_path = "test_img_ocr.png"
try:
    img = Image.open(image_path)
    print(f"Image chargée avec succès à {image_path}")
except Exception as e:
    print(f"Erreur lors de l'ouverture de l'image. Détails: {e}")

# Effectuer la reconnaissance de texte
try:
    text = pytesseract.image_to_string(img)
    print("Texte reconnu :")
    print(text)
except Exception as e:
    print(f"Erreur lors de l'exécution de la reconnaissance OCR. Détails: {e}")


'''
# Fonctionnement de `pytesseract` et du binaire `tesseract`

Non, Python ne charge pas directement le binaire `tesseract` dans sa mémoire lorsqu'il utilise `pytesseract`. Le processus fonctionne de manière différente :

### 1. Appel du binaire `tesseract` via une commande externe
- Lorsqu'on utilise `pytesseract` dans Python, le module envoie une commande système pour appeler le binaire `tesseract` et lui passer des arguments (par exemple, une image à traiter).
- `pytesseract` utilise la fonction `subprocess` pour exécuter le binaire `tesseract` dans un processus séparé. Ce processus est lancé en dehors de l'espace mémoire de Python, et Python interagit avec lui via l'entrée/sortie standard (stdin/stdout).

### 2. Pas de partage de mémoire directe
- **Le binaire `tesseract` est exécuté comme un processus distinct**, et non pas comme une partie du processus Python. Il n'est donc pas chargé directement dans l'espace mémoire de Python.
- La communication entre Python et Tesseract se fait via des échanges de données sur le système de fichiers ou via les flux (stdin et stdout), ce qui évite un partage direct de la mémoire.

### 3. Les résultats sont retournés via stdout
- Une fois l'OCR effectué par Tesseract, les résultats sont renvoyés sous forme de texte via la sortie standard (stdout). Python peut alors récupérer ce texte, le traiter, et le retourner à l'utilisateur.

### Conclusion
En résumé, **Python ne charge pas le binaire `tesseract` dans sa mémoire**. Au lieu de cela, il exécute `tesseract` en tant que processus externe et récupère les résultats en lisant la sortie du binaire. Cela permet à Python de fonctionner de manière indépendante de Tesseract, tout en utilisant ses fonctionnalités via des appels système.
'''

'''
# Échange de données entre Python et Tesseract via un pipe

Lorsque Python exécute `tesseract` via le module `subprocess`, il crée un **pipe** pour connecter les flux `stdout` de `tesseract` à `stdin` ou à un autre flux dans l'espace mémoire de Python. Ce mécanisme de redirection ne nécessite pas de copie explicite dans des fichiers temporaires ; les données sont échangées directement entre les processus via la mémoire partagée.

## Explication détaillée :

### 1. Le pipe comme canal de communication :
Le pipe fonctionne comme un **canal de communication** entre deux processus. Quand un processus (comme `tesseract`) écrit dans un pipe (stdout), l'autre processus (comme Python) peut immédiatement lire ce qui est écrit dans le pipe.

- Python, en utilisant `subprocess.PIPE` dans son appel, crée une connexion directe entre `tesseract` et Python via un pipe en mémoire.

### 2. Redirection de `stdout` vers Python :
Par défaut, `tesseract` écrit ses résultats dans son propre flux `stdout`. 

- Quand Python exécute `tesseract`, il redirige ce flux vers un pipe. Ce pipe n'écrit pas directement dans un fichier ; il "transporte" les données directement dans la mémoire RAM de Python.

### 3. Réception des données dans Python :
Python peut ensuite lire à partir du pipe comme s'il lisait à partir d'un fichier ou d'un flux. Le résultat de `tesseract` est donc disponible dans l'espace mémoire de Python, où il peut être manipulé.

Cela se fait via des fonctions comme `communicate()` dans `subprocess`, qui permet de capturer les données de `stdout` et de les stocker en mémoire.

## Illustration avec un exemple simple :

```python
import subprocess

# Appel de tesseract et redirection de stdout vers un pipe
process = subprocess.Popen(['tesseract', 'image.png', 'stdout'], stdout=subprocess.PIPE)

# Lecture de la sortie depuis le pipe
output, _ = process.communicate()

# Affichage du texte extrait
print(output.decode())
```

# Explication :

- subprocess.Popen(...) : Cette fonction lance le processus tesseract avec un argument stdout=subprocess.PIPE, ce qui crée un pipe entre tesseract et Python. Ainsi, au lieu d'écrire les résultats dans un fichier, tesseract les écrit dans ce pipe.
- process.communicate() : Cette méthode attend la fin de l'exécution de tesseract et récupère ce qui a été écrit dans le pipe (stdout), c'est-à-dire le texte extrait de l'image.
- output.decode() : Le texte extrait est récupéré en bytes, donc on le décode en chaîne de caractères pour l'afficher.

# Conclusion :

Oui, avec un pipe, la sortie de tesseract est redirigée directement dans la mémoire de Python via le flux stdout et le pipe, sans passer par un fichier intermédiaire. Cela constitue un exemple typique de communication inter-processus (IPC) où les données sont échangées directement dans l'espace mémoire sans nécessiter de processus d'écriture/lecture sur disque.
'''

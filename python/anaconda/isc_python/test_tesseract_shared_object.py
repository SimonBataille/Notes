'''
https://tesseract-ocr.github.io/tessapi/3.x/a00613.html
'''

import ctypes
import numpy as np
from PIL import Image
import pytesseract

# Charger la bibliothèque tesseract.so via ctypes
# find /home/simon/anaconda3/envs/isc_environment -iname "*tess*"
# /home/simon/anaconda3/envs/isc_environment/lib/libtesseract.so
# tesseract_lib = ctypes.CDLL('/path/to/tesseract.so')
tesseract_lib = ctypes.CDLL('/home/simon/anaconda3/envs/isc_environment/lib/libtesseract.so')

# Définir la signature de la fonction d'initialisation de l'API de Tesseract
# Par exemple, pour TessBaseAPIInit, nous devons connaître la signature exacte
# (cela pourrait varier selon la version de Tesseract et la fonction spécifique que tu souhaites utiliser).
# nm -D /home/simon/anaconda3/envs/isc_environment/lib/libtesseract.so | grep TessBaseAPIInit
# tesseract --version

# Initialisation de l'API de Tesseract
tesseract_lib.TessBaseAPIInit3.argtypes = [ctypes.POINTER(TessBaseAPI), ctypes.c_char_p, ctypes.c_char_p] # Chemin d'accès et langue
tesseract_lib.TessBaseAPIInit3.restype = ctypes.c_int

# Fonction pour créer l'objet TessBaseAPI via l'API tesseract
tesseract_lib.TessBaseAPICreate.restype = ctypes.POINTER(TessBaseAPI)
tesseract_lib.TessBaseAPICreate.argtypes = []

# Créer un objet TessBaseAPI via la fonction appropriée
tesseract_handle = tesseract_lib.TessBaseAPICreate()

# Chemin vers le répertoire contenant tessdata et la langue
datapath = b'/home/simon/anaconda3/envs/isc_environment/share/tessdata/'
language = b'eng'  # Langue pour l'OCR (ici l'anglais)


# Créer une instance de l'API Tesseract (en général, un objet TessBaseAPI)
# find /home/simon/anaconda3/envs/isc_environment -iname "*tess*"
# /home/simon/anaconda3/envs/isc_environment/share/tesseract-ocr/4.00/tessdata/
# ll /home/simon/anaconda3/envs/isc_environment/share/tessdata/
# api = tesseract_lib.TessBaseAPIInit(b'path/to/tessdata', b'eng')  # 'eng' pour l'anglais
api = tesseract_lib.TessBaseAPIInit3(tesseract_handle, datapath, language)  # 'eng' pour l'anglais

# Vérification de l'initialisation
if api != 0:
    print("Tesseract API initialized successfully.")
else:
    print("Failed to initialize Tesseract API.")

# Charger une image et la convertir en un format compréhensible par Tesseract
image = Image.open('test_img_ocr.png')

# Conversion de l'image en tableau numpy
image_data = np.array(image)

# Conversion du tableau numpy en une chaîne C pour la passer à Tesseract
image_ptr = ctypes.cast(image_data.ctypes.data, ctypes.POINTER(ctypes.c_uint8))

# Appeler la fonction de reconnaissance de texte (il faut adapter cette partie selon l'API exacte)
tesseract_lib.TessBaseAPIProcessPages.argtypes = [ctypes.POINTER(TessBaseAPI), ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p)]
tesseract_lib.TessBaseAPIProcessPages.restype = ctypes.c_char_p

# Exemple de texte reconnu
recognized_text = tesseract_lib.TessBaseAPIProcessPages(tesseract_handle, image_ptr, None)

if recognized_text:
    print("Recognized Text:", recognized_text.decode('utf-8'))
else:
    print("No text recognized.")

# Nettoyage et fermeture de l'API Tesseract
tesseract_lib.TessBaseAPIEnd.argtypes = [ctypes.POINTER(TessBaseAPI)]
tesseract_lib.TessBaseAPIEnd(tesseract_handle)

# Nettoyage et fermeture de l'API Tesseract
tesseract_lib.TessBaseAPIEnd(api)


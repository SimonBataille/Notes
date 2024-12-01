# Necessary packages
# !pip install datasets evaluate transformers[sentencepiece]

# Importation de la bibliothèque Hugging Face Transformers
from transformers import pipeline

# Création d'un pipeline pour l'analyse de sentiments
# 'sentiment-analysis' : Spécifie que le pipeline doit effectuer une classification de sentiments.
classifier = pipeline('sentiment-analysis')

# Analyse des sentiments pour une liste de phrases
# Les phrases données sont :
# - 'I am happy' : devrait retourner un sentiment positif.
# - 'I am sad' : devrait retourner un sentiment négatif.
results = classifier(['I am happy', 'I am sad'])

# Affichage des résultats d'analyse de sentiments
print("Sentiment Analysis Results:")
for result in results:
    print(result)

# Création d'un pipeline pour la traduction automatique
# 'translation' : Spécifie que le pipeline doit effectuer une traduction.
# 'model' : Utilise le modèle "Helsinki-NLP/opus-mt-fr-en", conçu pour traduire du français vers l'anglais.
traducer = pipeline('translation', model='Helsinki-NLP/opus-mt-fr-en')

# Traduction d'une phrase en français vers l'anglais
# 'Bonjour et bienvenu sur les videos de l'ISC' : sera traduit en anglais.
translation = traducer("Bonjour et bienvenu sur les videos de l'ISC")

# Affichage du résultat de la traduction
print("\nTranslation Result:")
print(translation)


'''
Explication du code :

    Analyse de sentiments :
        Utilise le pipeline 'sentiment-analysis' pour classifier le sentiment d'une phrase comme positif ou négatif.
        Les phrases ['I am happy', 'I am sad'] sont analysées.
        Les résultats incluent une étiquette (ex. POSITIVE, NEGATIVE) et un score de confiance.

    Traduction automatique :
        Le pipeline 'translation' utilise le modèle Helsinki-NLP/opus-mt-fr-en pour traduire du français vers l'anglais.
        La phrase "Bonjour et bienvenu sur les videos de l'ISC" est traduite.

    Affichage des résultats :
        Les résultats des deux pipelines sont affichés de manière lisible :
            Analyse de sentiments pour chaque phrase.
            Traduction automatique de la phrase en anglais.
'''

# Importation de la bibliothèque time et de Celery
import time
from celery import Celery

# Initialisation de l'application Celery
# La chaîne 'envoi_mails' est le nom de l'application Celery
# Le broker est un serveur Redis (localhost:6379) et nous utilisons Redis pour le backend aussi
app = Celery('envoi_mails', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Définition de la tâche asynchrone, utilisant le décorateur @app.task
# Cette tâche simule l'envoi d'un e-mail
@app.task
def envoi_mail(destinataire):
    # La fonction simule une attente de 1 secondes, comme l'envoi d'un e-mail réel
    time.sleep(1)

    # Impression de l'action de l'envoi du mail
    print('Envoi du mail a :', destinataire)

    # Retourne un dictionnaire simulant une réponse du système de messagerie
    # Le dictionnaire pourrait être utilisé pour vérifier l'état de l'envoi du mail
    return {'Envoi a ' + destinataire : 'OK'}

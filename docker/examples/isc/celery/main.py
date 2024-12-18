import time
from envoi_mails import envoi_mail

# 1. Test simple
# result  = envoi_mail.delay('DEST_1')
# print(result.get())


# 2. Test non bloquant
# result = envoi_mail.delay('DEST_1')  # Envoi de la tâche asynchrone

# # Attente non bloquante jusqu'à la fin de la tâche
# while not result.ready():
#     print('>>>>>')  # Affiche ">>>>>" pendant que la tâche est en cours
#     time.sleep(0.5)  # Attente de 0.5 seconde avant de vérifier à nouveau
# print('Fini !')
# print(result.get())  # Récupère le résultat une fois la tâche terminée


# 3. Test parallel
resultats = []

# on envoire 100 requetes d'un coup qui vont partir dans redis
# celery va lancer des workers et des taches en parallele (10 par defaut)
# il va mettre moins de 100 secondes pour les 100 mails !
for i in range(100):
    destinataire = f'DEST_{i}'
    resultats.append(envoi_mail.delay(destinataire))

fini = False
while not fini:
    fini = all(map(lambda r: r.ready(), resultats))
    print('>>>>>')
    time.sleep(0.5)
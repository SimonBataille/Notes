# import psycopg2
# import time
# import os

# # Variables d'environnement pour la connexion
# db_host = os.environ['DB_HOST']
# db_port = os.environ['DB_PORT']
# db_name = os.environ['DB_NAME']
# db_user = os.environ['DB_USER']
# db_password = os.environ['DB_PASSWORD']

# # Essayer de se connecter à PostgreSQL
# connected = False
# while not connected:
#     try:
#         print("Tentative de connexion à PostgreSQL...")
#         conn = psycopg2.connect(
#             host=db_host,
#             port=db_port,
#             dbname=db_name,
#             user=db_user,
#             password=db_password
#         )
#         connected = True
#         print("Connexion réussie à PostgreSQL !")
        
#         # Exemple : exécuter une requête
#         cursor = conn.cursor()
#         cursor.execute("SELECT version();")
#         print("Version de PostgreSQL :", cursor.fetchone())
#         cursor.close()
#         conn.close()
#     except psycopg2.OperationalError:
#         print("PostgreSQL n'est pas encore prêt. Nouvelle tentative dans 2 secondes...")
#         time.sleep(2)

import time

# Votre code principal ici
print("Le script a terminé ses tâches principales. Le conteneur reste actif.")

# Boucle infinie pour empêcher l'arrêt
while True:
    time.sleep(10)
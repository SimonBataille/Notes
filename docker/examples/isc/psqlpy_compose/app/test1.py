import psycopg2
import time
import os

# Variables d'environnement pour la connexion
db_host = os.environ.get('DB_HOST', 'localhost')  # Utilise 'localhost' par défaut si DB_HOST n'est pas défini
db_port = os.environ.get('DB_PORT', '5432')       # Utilise 5432 comme port par défaut
db_name = os.environ.get('DB_NAME', 'mydatabase')
db_user = os.environ.get('DB_USER', 'myuser')
db_password = os.environ.get('DB_PASSWORD', 'mypassword')

if not db_host or not db_name or not db_user or not db_password:
    raise ValueError("Certaines variables d'environnement nécessaires ne sont pas définies.")

# Essayer de se connecter à PostgreSQL
connected = False
while not connected:
    try:
        print("Tentative de connexion à PostgreSQL...")
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        connected = True
        print("Connexion réussie à PostgreSQL !")
        
        # Exemple : exécuter une requête
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        print("Version de PostgreSQL :", cursor.fetchone())
        cursor.close()
        conn.close()
    except psycopg2.OperationalError:
        print("PostgreSQL n'est pas encore prêt. Nouvelle tentative dans 2 secondes...")
        time.sleep(2)

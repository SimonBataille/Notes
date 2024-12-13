import psycopg2
import time
import os

# Variables d'environnement pour la connexion
db_host = os.environ.get('DB_HOST', 'localhost')
db_port = os.environ.get('DB_PORT', '5432')
db_name = os.environ.get('DB_NAME', 'mydatabase')
db_user = os.environ.get('DB_USER', 'myuser')
db_password = os.environ.get('DB_PASSWORD', 'mypassword')

# Fonction pour exécuter une requête SQL
def execute_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            print("Résultats de la requête :")
            for row in rows:
                print(row)
        else:
            conn.commit()
            print("Requête exécutée avec succès.")
        cursor.close()
    except psycopg2.ProgrammingError as e:
        print(f"Erreur de requête SQL : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

# Essayer de se connecter à PostgreSQL
connected = False
conn = None
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
        print("Prêt à recevoir des requêtes SQL (tapez 'quit' pour quitter).")
        
        # Boucle pour recevoir et exécuter des requêtes
        while True:
            query = input("Entrez une requête SQL : ")
            if query.lower() == 'quit':
                print("Fermeture de la connexion.")
                break
            execute_query(conn, query)
    except psycopg2.OperationalError:
        print("PostgreSQL n'est pas encore prêt. Nouvelle tentative dans 2 secondes...")
        time.sleep(2)
    except KeyboardInterrupt:
        print("\nInterruption détectée. Arrêt du script.")
        break
    finally:
        if conn:
            conn.close()
            print("Connexion fermée.")

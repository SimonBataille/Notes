import psycopg2

# Informations de connexion
db_host = "localhost"  # Docker expose PostgreSQL sur localhost:5432
db_port = "5432"
db_name = "mydatabase"
db_user = "myuser"
db_password = "mypassword"

try:
    # Connexion à PostgreSQL
    print("Tentative de connexion à PostgreSQL...")
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    print("Connexion réussie à PostgreSQL !")

    # Exemple : exécuter une requête
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    print("Version de PostgreSQL :", cursor.fetchone())

    # Fermer la connexion
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print("Erreur lors de la connexion à PostgreSQL :", e)

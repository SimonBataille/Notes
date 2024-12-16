# Launch postgresql-container
`docker run --name my-postgres-container -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres:alpine`

`docker ps`

`docker exec -it my-postgres-container psql -U myuser -d mydatabase`

`docker stop my-postgres-container`
`docker rm my-postgres-container`

`iptables -t nat -L -n`

# Venv Python
`python3 -m venv venv`

`source venv/bin/activate`

`pip install --upgrade pip`

`pip install psycopg2-binary`

`pip install SQLAlchemy`

`SELECT * FROM eleves;`

# Relationship
En résumé :

    Temporaire et logique : La relationship est une abstraction Python et fonctionne uniquement dans le cadre du contexte actuel (session SQLAlchemy).
    Aucune modification structurelle : Elle ne crée ni supprime de colonnes ou de tables dans la base.
    Lien en mémoire : La gestion des relations est effectuée en RAM tant que vous n'exécutez pas de commit.
    Requêtes SQL automatiques : SQLAlchemy traduit les accès via relationship en requêtes SQL uniquement lorsqu'un accès aux données est nécessaire

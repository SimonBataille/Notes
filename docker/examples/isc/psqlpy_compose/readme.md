# Host cli
`docker ps` : list containers
`docker exec -it postgres-container bash` : shell on already launched container
`docker exec -it python-app bash`
`docker logs postgres-container`

# second container launch
`docker run -it --rm --network <network_name> <image_name> bash` : docker run -it --rm --network psqlpy_mynetwork psqlpy-python-app bash
`cat /etc/resolv.conf`
`export DB_HOST='postgres-container'` : resolved by intern DNS 127.0.0.11 because postgres-container is a service in compose

# docker network
`docker network ls`
`docker network inspect <network_name>`
`docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name>`

# docker dns = 127.0.0.11, from container
`apt-get update && apt-get install -y dnsutils`
`dig postgres-container`

# postgres container cli
`ls /var/lib/postgresql/data`
`cat /var/lib/postgresql/data/postgresql.conf` : listen_addresses = '*'

`cat /var/lib/postgresql/data/pg_hba.conf` :
```
    local   replication     all                                     trust
    host    replication     all             127.0.0.1/32            trust
    host    replication     all             ::1/128                 trust
    host all all all scram-sha-256
```

`psql -U myuser -d mydatabase`
`\l` : bdd
`\du` : role

```
Lister les bases de données : \l
Se connecter à une base de données : \c <database_name>
Lister les tables : \dt
Lister les tables d’un schéma spécifique : \dt <schema_name>.*
Voir les détails d’une table : \d <table_name>
Quitter PostgreSQL : \q

Lister les schémas : \dn
Lister les tables d’un schéma : \dt <schema_name>.*
Lister tous les objets d’un schéma : \ds <schema_name>.*
```

# ping from postgres-container to python-app and dns resolution
En résumé :

    1. Le conteneur postgres-container envoie une requête DNS à 127.0.0.11.
    2. Docker traite cette requête via son serveur DNS interne et résout le nom python-app en une adresse IP, par exemple 172.18.0.3.
    3. Le conteneur postgres-container utilise l'adresse IP retournée pour communiquer avec python-app.
    4. Ce processus ne nécessite pas de communication avec l'hôte ou son moteur Docker, car tout se passe dans le réseau interne de Docker. 

# schema intern psql
La possibilité d'accéder aux tables internes de PostgreSQL, même lorsque vous êtes connecté à une base de données spécifique (autre que celles du schéma système pg_catalog), est liée à la structure de PostgreSQL et à la gestion des schémas système.
Pourquoi vous pouvez accéder aux tables internes (comme celles de pg_catalog) depuis n'importe quelle base de données ?

Voici l'explication détaillée :

    Schémas système :
        PostgreSQL organise les données en schémas, et pg_catalog est un schéma système spécial qui contient toutes les métadonnées nécessaires au bon fonctionnement du serveur PostgreSQL.
        Ce schéma est toujours accessible, peu importe la base de données à laquelle vous êtes connecté. C'est un mécanisme de partage global des métadonnées.

    Accès aux tables système à travers n'importe quelle base de données :
        PostgreSQL a été conçu pour que certains schémas système, comme pg_catalog, soient universellement accessibles, peu importe la base de données sur laquelle vous êtes connecté.
        pg_catalog contient des informations importantes sur toutes les bases de données et les objets dans le serveur PostgreSQL. Cela inclut les tables de la base de données, les types, les rôles, les index, etc.
        Cela permet à un utilisateur ou à un administrateur d’interroger la configuration et les objets de l’ensemble du serveur, même s’ils ne sont connectés qu’à une seule base de données.

    Raisons pratiques pour cet accès :
        Cela permet d’obtenir des informations globales sur l’état du serveur, même si vous êtes dans une base de données particulière. Par exemple, vous pouvez interroger les informations sur les rôles utilisateurs ou obtenir des statistiques globales sur les performances.
        Les bases de données dans PostgreSQL sont indépendantes les unes des autres, mais l’accès aux métadonnées globales est nécessaire pour l’administration du serveur et la gestion des objets (telles que les relations entre tables, index, et rôles).

    Accès aux autres schémas système :
        De plus, PostgreSQL permet également l'accès à d'autres schémas système comme information_schema (un autre schéma contenant des informations sur les objets et structures dans la base de données, mais d'une manière plus standardisée).
        Le schéma pg_catalog est la principale source d'informations internes et est toujours accessible à tous les utilisateurs disposant des permissions adéquates, indépendamment de la base de données à laquelle ils sont connectés.

Exemple pour comprendre :

Si vous êtes connecté à une base de données spécifique, par exemple mydb, vous pouvez toujours exécuter une requête comme :

SELECT * FROM pg_catalog.pg_class;

Cela renverra des informations sur toutes les tables dans toutes les bases de données, y compris celles dans pg_catalog. Cela peut vous permettre de voir les tables internes du serveur PostgreSQL, même si vous ne vous trouvez pas dans la base de données pg_catalog.
En résumé :

    pg_catalog est un schéma partagé et accessible depuis toutes les bases de données dans un serveur PostgreSQL, ce qui permet de consulter les métadonnées et la configuration du serveur.
    Cela a été conçu pour offrir une gestion centralisée des métadonnées, accessibles sans restrictions en étant connecté à n'importe quelle base de données.

Résumé :

    PostgreSQL crée un utilisateur postgres lors de l'installation. Cet utilisateur est un superutilisateur ayant accès à toutes les bases de données du serveur.
    Les informations de cet utilisateur (et des autres rôles) sont stockées dans la table pg_roles dans le schéma pg_catalog.
    Par défaut, le serveur PostgreSQL n'est pas sécurisé, il est donc important de configurer des méthodes d'authentification et de restreindre les connexions pour renforcer la sécurité du serveur.

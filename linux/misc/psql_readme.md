# 0. Question
Avec les commandes dans des blocks tabules, peux-tu reformater ce texte en Markdown brut dans une seule cellule, avec du texte entre balises ``` pour que je puisse copier/coller ?

# 1. System V

Sur antiX, PostgreSQL est un service de système V (https://linuxjourney.com/lesson/sysv-overview) sur le port 5432.

## Commands Linux
```bash
- service postgresql status  
- sudo service postgresql start/stop  
- sudo ss -tulnp --> écoute en TCP sur 5432 (⚠️ lancer une règle dans le firewall/iptables pour protéger les connexions sur le port 5432 de ma machine)  
- sudo netstat -tulnp
```


# 2. Postgresql

A l'installation de PostgreSQL, un user Linux "postgres" est créé avec les droits sur le processus Linux.  
⚠️ NPC : un user "postgres" est également présent dans la base de données PostgreSQL par défaut. C'est l'utilisateur qui a tous les droits.

Il est recommandé de créer un autre utilisateur dans la base de données PostgreSQL, de lui attribuer des droits spécifiques et de définir un mot de passe pour les connexions à distance.

Les fichiers à modifier sont :  
- `/etc/postgresql/<version>/main/pg_hba.conf`  
- `/etc/postgresql/<version>/main/postgresql.conf`  

Les fichiers contenant les bases de données sont situés ici :  
- `ls /var/lib/postgresql/15/main/base`  

## Commands Linux

    getent passwd postgres       # Vérifie l'existence de l'utilisateur Linux "postgres"
    sudo grep postgres /etc/shadow  # Vérifie le mot de passe et informations de l'utilisateur Linux

    sudo -u postgres psql        # Connexion à PostgreSQL en tant qu'utilisateur Linux "postgres"

## Commands PostgreSQL

    \?                           # Aide sur les commandes PostgreSQL
    \l                           # Liste les bases de données
    \c nom_de_la_base            # Se connecter à une base de données
    \dt                          # Voir les tables d'une base de données
    \d nom_de_la_table           # Informations sur une table
    \du                          # Montre tous les rôles existants sur le serveur
    \dn                          # Affiche les schémas d'une base de données
    \dt schema_name.*            # Affiche les tables d'un schéma

## Infos sur la table d'administration PostgreSQL

Les informations et les données de PostgreSQL sont stockées dans des tables internes, mais elles ne sont pas visibles directement avec une commande comme \dt car ces tables font partie des schémas systèmes, comme `pg_catalog` :  

    \dt pg_catalog.*             # Liste les tables du schéma système `pg_catalog`

Pour obtenir des informations sur les bases de données et les tables stockées dans PostgreSQL, tu peux interroger les tables du schéma `pg_catalog` :  

    SELECT * FROM pg_database;   # Liste les bases de données
    SELECT * FROM pg_user;       # Liste les utilisateurs PostgreSQL

PostgreSQL utilise des tables internes dans des schémas comme `pg_catalog` pour stocker toutes ses informations système (bases de données, utilisateurs, tables, etc.). Ce sont des tables gérées par PostgreSQL lui-même, et elles ne sont pas affichées dans le schéma public. Tes propres données et tables seront stockées dans `public` ou un autre schéma une fois que tu les créeras.

Les données de configuration et les métadonnées concernant les objets de la base de données PostgreSQL sont principalement stockées dans le schéma `pg_catalog` de la base de données `postgres`.


# 3. Create new db and new user

## psql

    CREATE USER new_user WITH PASSWORD 'password';
    CREATE DATABASE new_db OWNER new_user;
    GRANT ALL PRIVILEGES ON DATABASE new_db TO new_user;
    GRANT CONNECT ON DATABASE new_db TO new_user;
    GRANT CREATE ON DATABASE new_db TO new_user;
    GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO new_user;

## pg_hba.conf file

    sudo nano /etc/postgresql/<version>/main/pg_hba.conf

    # TYPE  DATABASE        USER            ADDRESS                 METHOD
    host    new_db          new_user        192.168.1.0/24          md5
    host    all             new_user        127.0.0.1/32            md5

## postgresql.conf file

    sudo nano /etc/postgresql/<version>/main/postgresql.conf

    listen_addresses = '*'
    listen_addresses = '192.168.1.100'  # Remplace par l'adresse IP de ton serveur PostgreSQL

## summary user creation

    CREATE USER new_user WITH PASSWORD 'password';  # création de l'utilisateur
    CREATE DATABASE new_db OWNER new_user;          # création de la db
    GRANT ALL PRIVILEGES ON DATABASE new_db TO new_user;  # attribution des privilèges pour CRUD

    host    new_db          new_user        192.168.1.0/24          md5  # new_user autorisé à se connecter depuis le réseau local
    host    all             all             127.0.0.1/32            scram-sha-256  # par défaut

    listen_addresses = 'localhost,192.168.1.10'  # écoute les adresses du réseau local
    #listen_addresses = 'localhost'              # par défaut


# 4. Restore from .tar file

## drop

    dropdb -h localhost -U new_user new_db  # From Linux
    sudo -u postgres dropdb -U postgres new_db

## dump

    pg_dump -U postgres -d new_db -F tar -f d:\backup\dvdrental.tar 

## restore

    pg_restore -U postgres -d dvdrental D:/backup/dvdrental.tar
    pg_restore -U new_user -d new_db D:/backup/dvdrental.tar
    pg_restore -h localhost -U new_user -d new_db ~/Documents/2024/GEEK/postgresql/dvdrental/dvdrental.tar
    pg_restore -h localhost -U new_user -d new_db --no-owner ~/Documents/2024/GEEK/postgresql/dvdrental/dvdrental.tar

    # Copy file to /tmp
    cp dvdrental /tmp  # Postgres doit avoir les droits sur le répertoire
    sudo -u postgres pg_restore -d new_db /tmp/dvdrental.tar  # Exécuter en tant que postgres pour éviter de saisir le mot de passe

## create

    sudo -u postgres createdb new_db

    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE new_db TO new_user;"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO new_user;"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO new_user;"
    sudo -u postgres psql -c "GRANT USAGE ON SCHEMA public TO new_user;"
    sudo -u postgres psql -c "GRANT CREATE ON SCHEMA public TO new_user;"

    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE new_db TO new_user; 
                              GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO new_user; 
                              GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO new_user; 
                              GRANT USAGE ON SCHEMA public TO new_user; 
                              GRANT CREATE ON SCHEMA public TO new_user;"

-- Accordez les droits nécessaires au schéma public
    GRANT USAGE ON SCHEMA public TO new_user;
    GRANT CREATE ON SCHEMA public TO new_user;

-- Si le schéma contient déjà des tables ou séquences, accordez les droits sur celles-ci
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO new_user;
    GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO new_user;

    sudo -u postgres psql -f grant_privileges.sql

## connect

    psql -h localhost -U new_user -d new_db

## revoke privileges

    sudo -u postgres psql -c "REVOKE ALL PRIVILEGES ON DATABASE new_db FROM new_user; 
                              REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM new_user; 
                              REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM new_user; 
                              REVOKE USAGE ON SCHEMA public FROM new_user; 
                              REVOKE CREATE ON SCHEMA public FROM new_user;"


# 5. Install pgAdmiin(pgAdmin https://www.pgadmin.org/download/pgadmin-4-apt/)

## Setup the repository

### Install the public key for the repository (if not done previously):
```bash
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg
```
### Create the repository configuration file:
```bash
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
```

## Install pgAdmin

### Install for both desktop and web modes:
```bash
sudo apt install pgadmin4
```

### Install for desktop mode only:  

    sudo apt install pgadmin4-desktop

### Install for web mode only:  
  
    sudo apt install pgadmin4-web

### Configure the webserver, if you installed pgadmin4-web:

    sudo /usr/pgadmin4/bin/setup-web.sh
    sudo PGADMIN_PLATFORM_TYPE=debian /usr/pgadmin4/bin/setup-web.sh


### Add PostgreSQL Server to pgAdmin

- In pgAdmin, click on the “Servers” menu on the left sidebar, then right-click and choose “Register” then select “Server” Enter a name for your server and switch to the “Connection” tab. Fill in the following details:

```
Host name/address: localhost
Port: 5432
Maintenance database: postgres
Username: postgres
Password: (Enter the password you set for the PostgreSQL user)
```

- Click “Save” to add the server.


## Link between apache and pgadmin
```bash
simon@antix1:/etc/apache2
$ grep -nr admin
mods-available/proxy_html.conf:76:# http://www.apachetutor.org/admin/reverseproxies
conf-available/pgadmin4.conf:1:WSGIDaemonProcess pgadmin processes=1 threads=25 python-home=/usr/pgadmin4/venv
conf-available/pgadmin4.conf:2:WSGIScriptAlias /pgadmin4 /usr/pgadmin4/web/pgAdmin4.wsgi
conf-available/pgadmin4.conf:4:<Directory /usr/pgadmin4/web/>
conf-available/pgadmin4.conf:5:    WSGIProcessGroup pgadmin
apache2.conf:13:# order to make automating the changes and administering the server as easy as
```

# 6. Tables internes
Les **tables internes de PostgreSQL** (celles qui gèrent la configuration et les métadonnées) sont stockées dans un schéma spécial appelé **`pg_catalog`**. Voici un aperçu de leur organisation :

### 1. **`pg_catalog` : Le schéma des métadonnées**
   - **`pg_catalog`** est un schéma système dans PostgreSQL qui contient des tables et des vues utilisées pour gérer la base de données elle-même.
   - Ce schéma est automatiquement créé lors de l'installation de PostgreSQL, et il contient des informations essentielles pour le bon fonctionnement du serveur PostgreSQL.

### 2. **Tables internes de `pg_catalog`**
   Voici quelques tables et vues importantes présentes dans `pg_catalog` :

   - **`pg_class`** : Contient les informations sur les objets de la base de données (tables, index, séquences, etc.). Cette table contient des métadonnées essentielles pour chaque objet dans la base de données.
   - **`pg_attribute`** : Contient les informations sur les colonnes de toutes les tables dans la base de données.
   - **`pg_database`** : Contient les informations sur les bases de données dans un serveur PostgreSQL.
   - **`pg_user`** : Contient des informations sur les rôles utilisateurs et leurs privilèges.
   - **`pg_roles`** : Contient des informations détaillées sur les rôles, incluant des rôles utilisateur, des groupes et leurs permissions.

### 3. **Autres schémas et tables**
   - **`pg_stat`** : Contient des statistiques sur l'exécution des requêtes et la performance du serveur PostgreSQL.
   - **`pg_temp`** : Contient des tables temporaires créées durant la session de l'utilisateur.
   - **`pg_tables`** : Vues qui listeront toutes les tables accessibles dans la base de données.
   - **`pg_indexes`** : Liste tous les index dans la base de données.

### 4. **Emplacement physique des données**
   Les tables de `pg_catalog` et toutes les données de PostgreSQL (y compris les tables d'application et de système) sont stockées dans le répertoire de données PostgreSQL. Par défaut, cela se situe dans le répertoire `PGDATA` sur le serveur.

   - Si vous utilisez un conteneur Docker, par exemple, PostgreSQL stocke les données dans un volume Docker. 
   - Sur une installation classique de PostgreSQL, le répertoire de données est souvent situé dans un chemin comme `/var/lib/postgresql/data`.

   **Exemple pour un conteneur Docker :**
   - Si vous avez configuré un volume pour les données de PostgreSQL, le répertoire de données sera stocké dans ce volume, et vous pourriez le retrouver à un emplacement comme `/var/lib/postgresql/data`.

### 5. **Accès aux tables internes**
   Vous pouvez consulter ces tables directement via SQL pour examiner les métadonnées, les utilisateurs, et autres configurations internes. Par exemple :
   
   ```sql
   SELECT * FROM pg_catalog.pg_class;
   ```

## En résumé :

- Les tables internes de PostgreSQL, telles que celles stockées dans le schéma pg_catalog, sont essentielles pour la gestion de la base de données, mais elles sont stockées physiquement dans le répertoire de données de PostgreSQL.
- Sur un conteneur Docker, ce répertoire est souvent mappé vers un volume Docker ou un chemin spécifique sur l'hôte.


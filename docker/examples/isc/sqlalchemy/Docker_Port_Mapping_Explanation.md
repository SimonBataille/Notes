Docker Port Mapping Explanation

Quand vous exposez un port local d'une machine hôte à un conteneur Docker via une commande comme celle-ci :

`docker run --name my-postgres-container -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres:alpine`

Voici comment la transmission des requêtes est gérée :

1. **Mappage du port :**
   - L'option `-p 5432:5432` signifie que vous mappez le port 5432 de votre machine hôte au port 5432 du conteneur.
   - Toute requête envoyée à `localhost:5432` (ou 127.0.0.1:5432) sur votre hôte sera redirigée vers le port 5432 à l'intérieur du conteneur Docker.

2. **Configuration du réseau Docker :**
   - Par défaut, Docker utilise un réseau de type `bridge`.
   - Docker configure automatiquement des règles NAT (Network Address Translation) sur l'hôte pour gérer cette redirection. Ces règles sont appliquées via `iptables`.

3. **Trafic entrant sur le port exposé :**
   - Lorsqu'une requête arrive sur le port 5432 de l'hôte, elle est interceptée par Docker grâce aux règles NAT.
   - Docker redirige ensuite ce trafic vers l'adresse IP interne du conteneur (par exemple, 172.17.0.2:5432).

4. **Résolution des IP internes :**
   - Si vous utilisez des noms de service ou des conteneurs interconnectés, Docker utilise un serveur DNS interne (souvent accessible à l'intérieur des conteneurs via 127.0.0.11) pour résoudre les noms en adresses IP internes.
   - Cependant, lorsque vous interagissez directement avec un conteneur exposé, vous utilisez l'adresse IP publique de l'hôte (localhost dans ce cas) et non le DNS interne.

5. **Règles iptables (routage) :**
   - Docker configure une chaîne dans `iptables` pour gérer le trafic. Vous pouvez visualiser les règles en exécutant :
     ```
     sudo iptables -t nat -L -n
     ```
   - La règle typique pour un conteneur exposant le port 5432 ressemblera à :
     ```
     DNAT       tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:5432 to:172.17.0.2:5432
     ```
   - Cela indique que le trafic TCP dirigé vers le port 5432 de l'hôte est redirigé vers l'adresse IP interne du conteneur sur le même port.

6. **Exemple de fonctionnement :**
   - Une application cliente en dehors de Docker envoie une requête à `localhost:5432`.
   - Cette requête est interceptée par Docker Engine via les règles NAT.
   - Docker transfère la requête au port 5432 du conteneur mappé.

7. **Avantages du mappage de ports :**
   - Vous pouvez exposer un conteneur à l'extérieur du réseau Docker sans modifier son réseau interne.
   - Cela permet à des applications externes (comme votre client PostgreSQL) d'accéder au service à l'intérieur du conteneur.

En résumé, Docker gère le trafic entre l'hôte et les conteneurs via des règles de routage (iptables) et un mécanisme de NAT. Cela rend transparent l'accès aux services dans les conteneurs via les ports exposés.

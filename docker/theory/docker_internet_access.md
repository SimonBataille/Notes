# Explication de l'accès Internet des conteneurs Docker

Oui, les conteneurs Docker accèdent à Internet via une passerelle par défaut configurée automatiquement par Docker lorsqu'un réseau de type bridge est utilisé. Voici comment cela fonctionne :

## Passerelle dans un réseau Bridge

Docker crée un réseau bridge par défaut (souvent nommé `docker0`) lors de l'installation.  
Ce réseau est associé à une interface réseau virtuelle sur l'hôte, également appelée `docker0`, qui agit comme une passerelle pour les conteneurs.

Pour voir la configuration :  
`ip addr show docker0`

Sortie typique :  
        3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP 
        link/ether 02:42:67:a1:b3:4e brd ff:ff:ff:ff:ff:ff 
        inet 172.17.0.1/16 scope global docker0

Ici, **172.17.0.1** est l’adresse de la passerelle sur le réseau `docker0`.

## Table de routage dans un conteneur

À l'intérieur d'un conteneur, exécutez :  
`route -n`

Sortie typique :  
        Destination Gateway Genmask Flags Metric Ref Use Iface 
        0.0.0.0 172.17.0.1 0.0.0.0 UG 0 0 0 eth0 
        172.17.0.0 0.0.0.0 255.255.0.0 U 0 0 0 eth0

- **0.0.0.0** : Représente toutes les destinations (Internet).  
- **172.17.0.1** : C’est la passerelle utilisée pour accéder à des destinations en dehors du réseau Docker.

## NAT (Network Address Translation)

Docker configure automatiquement une règle NAT sur l'hôte pour permettre aux conteneurs d'accéder à Internet. Vous pouvez vérifier ces règles avec :  
`sudo iptables -t nat -L -n`

Sortie typique :  
        Chain POSTROUTING (policy ACCEPT) MASQUERADE all -- 172.17.0.0/16 0.0.0.0/0

La règle **MASQUERADE** traduit les adresses IP des conteneurs en l’adresse IP publique de l’hôte lorsqu’ils communiquent avec l’extérieur.

## Résolution DNS

Docker configure automatiquement un fichier `/etc/resolv.conf` dans chaque conteneur pour résoudre les noms de domaine. Ce fichier pointe souvent vers un serveur DNS interne ou vers le DNS de l’hôte.

Exemple :  
`cat /etc/resolv.conf`

Sortie typique :  
        nameserver 127.0.0.11 options ndots:0


- **127.0.0.11** : Serveur DNS interne de Docker.

## Cas de la connexion Internet

- **Communication entre conteneurs** : Les paquets restent dans le réseau Docker (`docker0`) et transitent directement.  
- **Communication avec l'extérieur** : Les paquets passent par `172.17.0.1`, puis sont traduits via NAT et acheminés par l'interface réseau principale de l'hôte (par exemple, `eth0` ou `wlp2s0`).

## Tester la connectivité

Pour vérifier qu’un conteneur a accès à Internet :  
1. Entrez dans le conteneur :  
   `docker exec -it <container_name> sh`  
2. Testez un ping vers une adresse publique :  
   `ping google.com`

## Résumé

1. Les conteneurs utilisent le réseau `docker0` pour la communication interne.  
2. Ils accèdent à Internet via la passerelle `172.17.0.1`, avec une traduction NAT appliquée par Docker.  
3. Les noms de domaine sont résolus via un service DNS interne ou celui de l’hôte.  
4. Cette configuration est automatique pour les réseaux bridge par défaut, mais peut être personnalisée.


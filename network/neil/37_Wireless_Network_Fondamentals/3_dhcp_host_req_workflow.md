### Comment le WLC attribue une adresse IP du pool VLAN 22 alors que son interface de management est en 192.168.10.11 ?  

Si le **WLC a son interface de management en 192.168.10.11 (VLAN 10)** mais doit attribuer des adresses du **pool VLAN 22** à un client sur le **SSID Corporate (mappé sur VLAN 22)**, voici comment cela fonctionne :  

---

### 1. Contexte :  
- **WLC (Interface Management)** : 192.168.10.11 (sur VLAN 10).  
- **SSID Corporate** : Mappé au **VLAN 22**, mais le serveur DHCP est toujours **le WLC lui-même** (192.168.10.11).  
- **Pool DHCP pour VLAN 22** : 192.168.22.0/24 (par exemple, 192.168.22.10 à 192.168.22.254).  

Cela est **parfaitement faisable**, car **le WLC agit comme un relais DHCP interne** pour les VLANs clients, même si l’interface de management est sur un VLAN différent.

---

### 2. Comment ça fonctionne :

1. **Le client sur le VLAN 22 envoie une requête DHCP Discover**.  
   - La requête passe par l’AP et est encapsulée dans **CAPWAP**.  
   - L’AP transmet cette requête au **WLC**.  

2. **Le WLC décode la trame CAPWAP et voit que la requête provient du VLAN 22**.  
   - Bien que l’adresse de management du WLC soit **192.168.10.11**, le WLC sait que cette requête concerne le **VLAN 22** grâce au mapping SSID–interface.  
   - **Le WLC redirige la requête vers son propre service DHCP interne**, spécifiquement pour le pool du VLAN 22.

3. **Le WLC attribue une adresse IP du pool VLAN 22 (192.168.22.x)**.  
   - Il répond directement au client avec une **DHCP Offer**, fournissant une adresse IP dans le **pool du VLAN 22** (par exemple, **192.168.22.10**).  

4. **Le client reçoit l’adresse IP sur VLAN 22**, et les communications normales peuvent commencer.

---

### 3. Pourquoi cela fonctionne même si l’adresse du WLC est en VLAN 10 ?  
Le **WLC peut gérer plusieurs interfaces virtuelles (SVI)** pour différents VLANs clients, même s’il n’a **qu’une seule adresse de management (192.168.10.11)**.

- L’interface de management est utilisée pour **administrer le WLC** et pour certaines fonctions CAPWAP, mais cela **n’empêche pas le WLC d’agir comme serveur DHCP sur d’autres VLANs**.  
- **Le service DHCP du WLC est multi-VLAN**, et chaque pool est associé à une interface spécifique (VLAN 22 dans ton cas).

---

### Exemple de configuration du pool DHCP sur le WLC pour VLAN 22 :

```plaintext
WLC(config)# config dhcp create pool VLAN22 
WLC(config)# config dhcp address-pool VLAN22 192.168.22.10 192.168.22.254 
WLC(config)# config dhcp network VLAN22 192.168.22.0 255.255.255.0 
WLC(config)# config dhcp enable pool VLAN22
```

Le **pool VLAN22** est maintenant actif, même si le **WLC est accessible via 192.168.10.11**.

---

### Résumé :  
1. Le **WLC reçoit la requête DHCP via CAPWAP** et identifie que la requête concerne **VLAN 22**.  
2. **Le WLC attribue une IP du pool 192.168.22.0/24**, bien que son interface de management soit sur **192.168.10.11**.  
3. Cela est possible grâce à la **gestion multi-VLAN interne du WLC**.

Dis-moi si tu veux un schéma pour clarifier cela visuellement ! 😊


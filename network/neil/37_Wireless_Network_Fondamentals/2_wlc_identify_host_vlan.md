### Comment le WLC sait-il que c'est pour le VLAN 23 dans ce cas ?  

Le **WLC** sait que la requête DHCP doit être associée au **VLAN 23** grâce au **SSID** et à l'interface mappée à ce VLAN. Voici le détail du mécanisme :  

---

### 1. Association SSID – Interface VLAN sur le WLC  
Lorsque tu configures le WLC, tu mappes chaque **SSID** à une **interface réseau spécifique**, qui elle-même est associée à un **VLAN**.  

**Exemple :**  
- **SSID : Corporate**  
  - Mappé à l'**interface Corporate** sur le WLC.  
  - Interface Corporate → **VLAN 23**, avec une adresse IP de gestion **192.168.23.11**.  
  - Serveur DHCP spécifié : **192.168.10.11**.  

Chaque paquet CAPWAP qui arrive sur le WLC est accompagné d’informations **indiquant à quel SSID et VLAN** appartient le client.

---

### 2. Processus détaillé : Requête DHCP Discover  
Quand un **hôte se connecte au SSID Corporate** :  
1. L’**AP encapsule le paquet DHCP Discover** dans un **tunnel CAPWAP** et l’envoie au **WLC**.  
2. Le WLC **décode les métadonnées du tunnel CAPWAP**, qui indiquent que ce paquet provient du **SSID Corporate** (donc du VLAN 23).  
3. Le WLC transmet cette requête au **serveur DHCP** en tant que **DHCP relay**, en précisant que c’est une requête pour le **VLAN 23**.

---

### 3. DHCP Relay avec l’option 82 (Agent Relay)  
Pour les environnements DHCP complexes, le WLC peut utiliser l’**option 82** (relay agent information) dans la requête DHCP.  
L’option 82 ajoute des métadonnées dans la requête pour préciser :  
- **Le VLAN ou l’interface d’origine**.  
- **Le SSID spécifique** associé à la requête.  

Cela permet au serveur DHCP de savoir précisément à quel pool d’adresses IP répondre.

---

### Exemple pratique :  
- **Hôte sur VLAN 23 (SSID Corporate)** envoie un **DHCP Discover**.  
- Le WLC l’interprète comme une requête pour le **VLAN 23** et la redirige vers **192.168.10.11**.  
- Le serveur DHCP retourne une adresse IP du **pool VLAN 23** (192.168.23.x).

---

### Conclusion :  
Le **WLC identifie le VLAN** de l’hôte grâce à :  
1. **L’association SSID-Interface VLAN** configurée sur le WLC.  
2. Les **métadonnées du tunnel CAPWAP**, qui indiquent de quel SSID la requête DHCP provient.  
3. Optionnellement, **l’option 82 DHCP relay**.  

Si tu veux, je peux te montrer un exemple concret avec **WLC et DHCP** pour vérifier ces paramètres ! 😊


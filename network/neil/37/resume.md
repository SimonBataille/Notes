0. Les APs ont deja une ip en 192.168.10.0/24 car :
  - il y'a un DHCP qui tourne sur le WLC(192.168.10.11)
  - les requetes DHCP sont acheminees jusqu'au WLC via les ports access VLAN 10 (APs->switch) ou trunk 10,22,23 (switch->WLC)

1. Ajout du server Radius dans Security > AAA > Radius > Authentication > New

2. DHCP dans Controller > DHCP scope
  - 'Corporate' (192.168.22.0/24, DNS : 192.168.11.10)
  - 'Guest' (192.168.23.0/24, DNS : 192.168.11.10)
  - /!\ les DHCPs tournent sur le WLC 192.168.10.11

3. Interfaces logiques sur WLC dans Controllers > Interfaces
  - interface 'Corporate' (VLAN 22 sur port physique 1 linked to g1/0/5 du switch)
    - VLAN 22, ip 192.168.22.1, gateway 192.198.22.1, /!\ DHCP server 192.168.10.11 /!\
  - interface 'Corporate' (VLAN 22 sur port physique 1 linked to g1/0/5 du switch)
    - VLAN 23, ip 192.168.23.1, gateway 192.198.22.1, /!\ DHCP server 192.168.10.11 /!\
  - WLC sait comment router sur 192.168.10.11 les requetes DHCP issues des hosts corporate ou guest 

4. WLANs 'Corporate' et 'Guest' dans WLANs > create new
  - Type WLAN, profile name 'corporate', SSID 'Corporate', ID '1'
    - general : Interface 'Corporate' (comme definie en 3)
    - security : WPA+WPA2, 802.1x
    - AAA Server : 192.168.11.10 port 1812
  - Type WLAN, profile name 'guest', SSID 'Guest', ID '2'

### 0. Les APs ont déjà une IP en 192.168.10.0/24 car :
  - Un serveur DHCP tourne sur le **WLC (192.168.10.11)** pour fournir des adresses dans **192.168.10.0/24**.  
  - Les requêtes DHCP sont acheminées vers le WLC via :  
    - **Ports access VLAN 10** (APs → Switch),  
    - **Port trunk (10, 22, 23)** entre le **Switch et le WLC**.

---

### 1. Configuration du serveur RADIUS :
Dans **Security > AAA > Radius > Authentication > New**, ajoutez le serveur RADIUS :  
  - **Adresse** : 192.168.11.10  
  - **Port** : 1812  
  - **Secret partagé** : …  

---

### 2. Configuration des scopes DHCP :
Dans **Controller > DHCP Scope**, configurez les scopes DHCP :  
  - **Corporate** : 192.168.22.0/24, DNS : 192.168.11.10  
  - **Guest** : 192.168.23.0/24, DNS : 192.168.11.10  
  - **Attention :** Ces DHCP scopes tournent également sur le **WLC (192.168.10.11)**.

---

### 3. Création des interfaces logiques sur le WLC :
Dans **Controller > Interfaces**, configurez les interfaces :  

  - **Interface 'Corporate'** :  
    - **VLAN 22**, IP 192.168.22.1, **Gateway 192.168.22.1**,  
    - **DHCP server : 192.168.10.11**,  
    - Mappée au port physique 1 du WLC (lié à **g1/0/5 sur le switch**).  

  - **Interface 'Guest'** :  
    - **VLAN 23**, IP 192.168.23.1, **Gateway 192.168.23.1**,  
    - **DHCP server : 192.168.10.11**,  
    - Mappée au port physique 1 du WLC (lié à **g1/0/5 sur le switch**).  

Le **WLC sait router les requêtes DHCP** issues des **hosts Corporate (VLAN 22)** et **Guest (VLAN 23)** vers le **DHCP interne 192.168.10.11**.

---

### 4. Configuration des WLANs :  
Dans **WLANs > Create New**, créez les WLANs :

  - **Corporate (SSID : Corporate)** :  
    - **Type : WLAN**, **Profile Name : corporate**, **ID : 1**  
    - **General :** Interface ‘Corporate’ (comme définie en 3)  
    - **Security :** WPA+WPA2, 802.1x  
    - **AAA Server :** 192.168.11.10, port 1812  

  - **Guest (SSID : Guest)** :  
    - **Type : WLAN**, **Profile Name : guest**, **ID : 2**  
    - **General :** Interface ‘Guest’ (comme définie en 3)  
    - **Security :** WPA+WPA2, 802.1x  
    - **AAA Server :** 192.168.11.10, port 1812  


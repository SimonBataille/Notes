
# Rôle de `switchport trunk native vlan 20` pour la gestion IP sur un switch Cisco

La commande `switchport trunk native vlan 20` contribue à établir un lien **indirect** entre un port physique (comme `GigabitEthernet0/1`) et une adresse IP configurée sur une interface VLAN (par exemple, `192.168.20.7`). Voici une explication détaillée.

---

## 1. Contexte

### Configuration d'une interface VLAN pour la gestion
Une adresse IP est configurée sur l’interface VLAN 20 pour permettre la gestion du switch :
```bash
Switch(config)# interface vlan 20
Switch(config-if)# ip address 192.168.20.7 255.255.255.0
Switch(config-if)# no shutdown
```
- Cela rend le switch joignable via l’adresse IP `192.168.20.7` dans le réseau du VLAN 20.

### Configuration d’un port trunk
Un port physique (comme `GigabitEthernet0/1`) est configuré en mode trunk pour transporter plusieurs VLANs, avec un VLAN natif défini :
```bash
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk native vlan 20
```
- Le VLAN natif sur ce port trunk est défini comme le VLAN 20.

---

## 2. Rôle de `switchport trunk native vlan 20`

La commande `switchport trunk native vlan 20` effectue les actions suivantes :
1. Associe toutes les **trames non taguées** reçues sur `GigabitEthernet0/1` au VLAN 20.
2. Transmet toutes les trames du VLAN 20 sur ce port **sans tag**.

### Pourquoi cela est important
- Les trames non taguées traversant le port trunk sont correctement associées au VLAN 20.
- Cela permet au switch de router les trames du VLAN 20 vers l’interface VLAN 20, qui agit comme une passerelle IP.

---

## 3. Établir un lien indirect avec l'adresse IP
L'interface VLAN 20 (SVI) agit comme une interface logique associée à tout le trafic du VLAN 20 sur le switch. 

- **Avec `switchport trunk native vlan 20`** :
  - Les trames non taguées reçues sur le port trunk sont associées au VLAN 20.
  - Ces trames peuvent être traitées par l'interface VLAN 20, qui possède l’adresse IP `192.168.20.7`.

### Résultat
Même si le port physique `GigabitEthernet0/1` transporte plusieurs VLANs, le fait de définir un VLAN natif (VLAN 20) permet d'établir une connexion logique entre ce port et l’adresse IP configurée sur l'interface VLAN 20.

---

## 4. Résultat final : Pinger le switch

Avec cette configuration, le switch est joignable via `192.168.20.7` si :
1. Un appareil est connecté au VLAN 20 :
   - Soit directement via un port access.
   - Soit via un autre switch avec un port trunk transportant le VLAN 20.
2. Les trames du VLAN 20 atteignent l'interface VLAN 20 du switch.

---

## 5. Résumé

- **Interface VLAN 20** : Fournit une adresse IP (`192.168.20.7`) pour la gestion du VLAN 20.
- **Commande `switchport trunk native vlan 20`** :
  - Associe les trames non taguées reçues sur le port trunk au VLAN 20.
  - Fait en sorte que le VLAN 20 soit correctement acheminé vers l'interface VLAN 20.
- Cette configuration permet au switch d'être joignable via une adresse IP, à condition que le trafic du VLAN 20 soit correctement acheminé.

Si vous avez des questions sur la configuration ou la gestion des VLANs, n'hésitez pas à demander !

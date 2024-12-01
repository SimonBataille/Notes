
# Configuration des interfaces VLAN et des ports trunk sur un routeur/switch Cisco

Voici une explication détaillée des concepts liés à la configuration d'une **interface VLAN**, d'un **port trunk** et d'un **VLAN natif** sur un équipement Cisco.

---

## 1. Création d'une interface VLAN
Une **interface VLAN** (appelée aussi SVI - Switch Virtual Interface) est une interface logique associée à un VLAN spécifique.

### Utilisations de l'interface VLAN :
- Fournir une connectivité IP au VLAN.
- Gérer le switch (via SSH, telnet, etc.).
- Permettre la communication entre VLANs sur un switch de niveau 3 (routage inter-VLAN).

### Exemple de configuration :
```bash
Switch(config)# interface vlan 20
Switch(config-if)# ip address 192.168.20.1 255.255.255.0
Switch(config-if)# no shutdown
```

- **Explication :**
  - Une interface virtuelle pour le VLAN 20 est créée avec l’adresse IP `192.168.20.1`.
  - Cette configuration ne modifie pas directement les ports physiques.

---

## 2. Configuration des ports physiques

### a. **Mode access (pour un VLAN spécifique)**
- Le mode access associe un port à un seul VLAN.
- Utilisé pour connecter un PC, un serveur ou tout autre équipement à un VLAN spécifique.

#### Exemple de configuration :
```bash
Switch(config)# interface FastEthernet0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 20
```

### b. **Mode trunk (pour plusieurs VLANs)**
- Le mode trunk permet à un port de transporter le trafic de plusieurs VLANs.
- Le **VLAN natif** est utilisé pour les trames non taguées.

#### Exemple de configuration avec VLAN 20 comme VLAN natif :
```bash
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk native vlan 20
```

- **Explication :**
  - Le port en mode trunk transportera le trafic de plusieurs VLANs.
  - Les trames non taguées seront associées au VLAN 20 (VLAN natif).

---

## 3. Relation entre SVI, VLAN natif et trunk

### a. **Interface VLAN (SVI)**
- Une SVI est une interface logique associée à un VLAN pour fournir une connectivité IP ou une interface de gestion.

### b. **Mode trunk**
- Un port en mode trunk permet à plusieurs VLANs de partager un lien physique.
- Les trames non taguées utilisent le VLAN natif défini.

### c. **Exemple de workflow**
1. **Création d’une interface VLAN 20 (SVI) :**
   ```bash
   Switch(config)# interface vlan 20
   Switch(config-if)# ip address 192.168.20.1 255.255.255.0
   Switch(config-if)# no shutdown
   ```

2. **Configuration d’un port en mode trunk avec VLAN 20 comme VLAN natif :**
   ```bash
   Switch(config)# interface GigabitEthernet0/1
   Switch(config-if)# switchport mode trunk
   Switch(config-if)# switchport trunk native vlan 20
   ```

- **Résultat :**
  - L'interface VLAN 20 fournit une connectivité IP pour le VLAN 20.
  - Le port trunk transporte le trafic de plusieurs VLANs, avec le VLAN natif défini pour les trames non taguées.

---

## Résumé

| **Concept**          | **Description**                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| **Interface VLAN (SVI)** | Fournit une adresse IP pour un VLAN.                                          |
| **Port access**       | Associe un port à un seul VLAN (mode access).                                  |
| **Port trunk**        | Permet à un port de transporter le trafic de plusieurs VLANs.                  |
| **VLAN natif**        | Définit le VLAN utilisé pour le trafic non tagué sur un port trunk.            |

---

Si vous avez d'autres questions sur la configuration des VLANs ou des ports sur des équipements Cisco, n'hésitez pas !


# Relation entre VLAN 20, l'interface VLAN et le port trunk GigabitEthernet0/1

Dans un routeur ou un switch de niveau 3, un lien **indirect** est établi entre le VLAN 20 et le port trunk (`GigabitEthernet0/1`) pour router le trafic. Voici une explication détaillée.

---

## 1. Rôle du port `GigabitEthernet0/1` en mode trunk

### Fonction du port trunk
- Le port trunk (`GigabitEthernet0/1`) est configuré pour transporter le trafic de plusieurs VLANs, y compris le VLAN 20.
- Il agit comme un **chemin physique** pour les trames étiquetées (taguées) ou non étiquetées (trafic du VLAN natif).

#### Ce que fait le port trunk pour le VLAN 20
1. Si une trame appartient au VLAN 20 (taguée ou non), elle est transportée via le port trunk.
2. Le switch/routeur identifie le VLAN de la trame et la transmet à l'interface VLAN logique appropriée (SVI).

---

## 2. Rôle de l’interface VLAN 20 (SVI)

### Fonction de l'interface VLAN (SVI)
L’interface VLAN 20 agit comme une **passerelle logique** pour le VLAN 20. Elle permet :
1. De fournir une adresse IP pour le VLAN 20 (par exemple, 192.168.20.1).
2. D'effectuer le **routage inter-VLAN** pour permettre la communication avec d'autres VLANs ou réseaux.

#### Exemple de configuration :
```bash
interface vlan 20
 ip address 192.168.20.1 255.255.255.0
 no shutdown
```

#### Entrée dans la table de routage
La table de routage affiche le réseau VLAN 20 comme directement connecté via l'interface VLAN 20 :
```
C    192.168.20.0/24 is directly connected, Vlan20
```

---

## 3. Lien entre VLAN 20 et le port `GigabitEthernet0/1`

Bien que le port trunk transporte le trafic du VLAN 20, il n’apparaît pas directement dans la table de routage. Le lien est **indirectement établi** grâce à la configuration suivante :

#### Exemple de configuration du port trunk :
```bash
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 20,30,40
 switchport trunk native vlan 20
```

### Ce lien permet :
1. Le transport des trames taguées du VLAN 20.
2. L’acheminement des trames non taguées (si le VLAN 20 est configuré comme VLAN natif).

L’interface VLAN 20 (SVI) agit ensuite comme passerelle pour router ce trafic vers d'autres réseaux ou VLANs.

---

## 4. Comment le trafic est routé

Lorsqu'une trame du VLAN 20 est reçue sur le port trunk :
1. Le switch identifie le VLAN de la trame (via le tag VLAN ou la configuration de VLAN natif).
2. Si la destination est hors du VLAN 20, le routage inter-VLAN est effectué par l’interface VLAN 20.
3. La trame est ensuite routée vers le port approprié pour atteindre sa destination (un autre port trunk ou un port access).

---

## 5. Résumé

- **Le port `GigabitEthernet0/1` est lié au VLAN 20 via sa configuration en mode trunk.**
  - Il transporte les trames taguées du VLAN 20 ainsi que les trames non taguées si le VLAN natif est 20.

- **L'interface VLAN 20 (SVI) effectue le routage.**
  - Elle agit comme une passerelle logique pour le VLAN 20 (`192.168.20.0/24`).
  - La table de routage pointe vers cette interface logique (`Vlan20`).

- **Le lien entre VLAN 20 et `GigabitEthernet0/1` est indirect.**
  - Le port physique sert uniquement à transporter les trames, tandis que l’interface VLAN gère le routage.

---

Si vous avez des questions supplémentaires sur le routage ou la configuration des VLANs, n'hésitez pas !

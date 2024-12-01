
# Port Trunk et Table MAC dans un Switch ou Routeur Cisco

Lorsqu’un port trunk comme `GigabitEthernet0/1` est utilisé, la table MAC du switch ou du routeur enregistre les adresses MAC des appareils connectés aux VLANs qui passent par ce port. Voici comment cela fonctionne.

---

## 1. Fonctionnement de la table MAC

La table MAC d’un switch ou d’un routeur associe :
- Une **adresse MAC** d’un appareil à un **port physique**.
- Cela permet au switch de savoir par quel port transmettre les trames destinées à une adresse MAC spécifique.

---

## 2. Port trunk et table MAC

Un port trunk (par exemple, `GigabitEthernet0/1`) transporte les trames de plusieurs VLANs. Dans ce cas :
- Le switch associe les adresses MAC des appareils connectés sur différents VLANs à ce port trunk.
- Par exemple :
  - Si une machine du VLAN 20 est connectée au switch via ce port trunk, son adresse MAC sera associée au VLAN 20 et au port `GigabitEthernet0/1`.
  - Si des appareils d'autres VLANs utilisent également ce port trunk, leurs adresses MAC seront également associées à ce port.

---

## 3. Exemple : Machine dans le VLAN 20

Supposons qu’une machine avec l’adresse MAC **`AA:BB:CC:DD:EE:FF`** soit connectée au VLAN 20 via un autre switch, et que le trafic passe par le port trunk `GigabitEthernet0/1`. Voici ce qui se passe :
- Le switch apprend que **l’adresse MAC `AA:BB:CC:DD:EE:FF`** appartient au VLAN 20.
- La table MAC enregistre cette association :
  ```
  VLAN   MAC Address         Port
  ----   -----------------   -----
  20     AA:BB:CC:DD:EE:FF   Gi0/1
  ```

---

## 4. Gestion de plusieurs VLANs sur un port trunk

Si plusieurs VLANs utilisent le port trunk, la table MAC inclura des entrées pour chaque VLAN :

Exemple :
```
VLAN   MAC Address         Port
----   -----------------   -----
10     11:22:33:44:55:66   Gi0/1
20     AA:BB:CC:DD:EE:FF   Gi0/1
30     FF:EE:DD:CC:BB:AA   Gi0/1
```

- Chaque entrée est contextualisée par le VLAN :
  - Cela garantit que le trafic des VLANs reste isolé même lorsqu’il partage le même port physique.

---

## 5. Résumé

- Oui, le port trunk `GigabitEthernet0/1` apparaîtra dans la table MAC pour **toutes les adresses MAC** des appareils connectés via ce port, y compris celles du VLAN 20.
- Cependant, la table MAC inclura également les adresses MAC des appareils d’autres VLANs passant par le port trunk.
- Chaque entrée est associée à un VLAN spécifique, ce qui permet de gérer correctement le trafic entre VLANs tout en utilisant un port physique partagé.

Si vous avez des questions sur le fonctionnement des VLANs ou des tables MAC, n’hésitez pas à demander !

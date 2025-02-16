### 1. Structure réseau pour GRE entre deux sites
**Pré-requis :**
- Chaque site a un **routeur avec une interface connectée à Internet**. Cette interface doit avoir une **IP publique routable**.  
- Un **tunnel GRE** est configuré entre les deux **adresses IP publiques des routeurs**.

---

### 2. Fonctionnement du routage GRE sur Internet

#### **Étapes détaillées :**

1. **Site A encapsule un paquet dans GRE** :  
   Le routeur du **site A** encapsule le paquet (par exemple, une mise à jour OSPF ou un paquet multicast) avec un **en-tête GRE** et un **en-tête IP externe**.  

   **Exemple de paquet encapsulé :**
```
[ IP Header (Source: 10.0.0.1, Destination: 20.0.0.1) ] [ GRE Header ] [ Original Packet (Multicast, IPv6, etc.) ]
```

- **10.0.0.1** : IP publique du site A  
- **20.0.0.1** : IP publique du site B  

2. **Transmission sur Internet** :  
Le paquet GRE est **routé sur Internet** comme n’importe quel paquet IP classique, utilisant les adresses **10.0.0.1** et **20.0.0.1** pour la livraison. Les routeurs Internet ne savent pas que ce paquet contient du GRE encapsulé — ils voient simplement un paquet IP ordinaire.

3. **Décapsulation au site B** :  
Le **routeur du site B** reçoit le paquet, **décapsule l’en-tête GRE**, et extrait le paquet d’origine.  
Il peut ensuite le traiter normalement (par exemple, une mise à jour OSPF ou un paquet multicast est traité comme s’il venait directement du site A).

4. **Réponse en sens inverse** :  
Le **site B encapsule à son tour** les paquets de réponse et les envoie à **10.0.0.1** (site A), en suivant le même processus.

---

### 3. Exemple avec IPs publiques

- **Site A :**  
- IP publique : 10.0.0.1  
- Tunnel GRE : **Tunnel 0, IP 192.168.1.1/24**  

- **Site B :**  
- IP publique : 20.0.0.1  
- Tunnel GRE : **Tunnel 0, IP 192.168.1.2/24**  

**Configuration du tunnel sur Site A :**
```
interface Tunnel 0 ip address 192.168.1.1 255.255.255.0 tunnel source 10.0.0.1 tunnel destination 20.0.0.1
```

**Configuration sur Site B :**
```
interface Tunnel 0 ip address 192.168.1.2 255.255.255.0 tunnel source 20.0.0.1 tunnel destination 10.0.0.1
```
---

### 4. Comment le paquet est routé :
1. **Paquet d’origine :** Multicast ou paquet non-IP à encapsuler.  
2. **En-tête GRE ajouté** pour l’encapsulation.  
3. **En-tête IP externe** avec les adresses IP publiques des deux sites.  
4. **Routage IP standard sur Internet** : Les paquets passent par des routeurs Internet jusqu’à atteindre l’IP publique du site B.

---

### Résumé :
- Chaque site doit avoir un **routeur avec une IP publique** pour établir un **tunnel GRE sur Internet**.  
- **Les paquets GRE sont routés comme des paquets IP classiques** entre les deux adresses publiques.  
- GRE permet de transporter du **multicast, de l’IPv6, ou du trafic non-IP**, même si Internet ne les supporte pas directement.

Dis-moi si tu veux que je te montre un schéma pour rendre cela visuel ! 😊


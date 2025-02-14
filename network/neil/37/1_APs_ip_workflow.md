### 1. Obtention de l’adresse IP via DHCP
Les **APs**, étant sur des **ports access VLAN 10**, envoient une requête **DHCP Discover** pour obtenir une adresse IP.

Le serveur DHCP leur fournit :
- **Adresse IP** sur le VLAN 10 (par exemple, 192.168.10.101).  
- **Masque de sous-réseau** et **passerelle**.  
- **Option 43 (si configurée)** : L’adresse IP du **WLC** (par exemple 192.168.10.11).  

---

### 2. Recherche du WLC (Discovery Process)
Après avoir obtenu son adresse IP, l’AP cherche à découvrir le **WLC**. Il suit ces étapes :  

1. **DHCP Option 43 (si disponible)** :  
   Si l’option 43 est configurée dans la réponse DHCP, l’AP utilise l’adresse IP du WLC fournie par cette option.  
   C’est la méthode la plus fiable et rapide.  

2. **DNS (méthode secondaire)** :  
   Si l’option 43 n’est pas disponible, l’AP cherche un enregistrement DNS pour `cisco-capwap-controller.localdomain`.  
   Il interroge le serveur DNS pour obtenir l’adresse IP du WLC.  

3. **Broadcast sur le VLAN 10 (méthode de dernier recours)** :  
   Si aucune des méthodes précédentes ne fonctionne, l’AP envoie une requête **broadcast CAPWAP** sur le VLAN 10 pour trouver le WLC.

---

### 3. Établissement du tunnel CAPWAP
Une fois le WLC découvert :
1. L’AP initie une session **CAPWAP sur UDP 5246 (contrôle)** avec le WLC.  
2. Une fois authentifié et configuré, l’AP utilise **UDP 5247 (données)** pour transmettre le trafic utilisateur.  

---

### Configuration de l’option 43 sur le serveur DHCP :
Sur un serveur DHCP Cisco, l’option 43 peut être configurée ainsi :

```plaintext
ip dhcp pool AP-VLAN10
   network 192.168.10.0 255.255.255.0
   default-router 192.168.10.1
   option 43 hex f104c0a80a0b   ! (f1 = sub-option 1, 04 = 4 bytes, c0a80a0b = 192.168.10.11)
```

## Résumé :

1. **Les APs obtiennent une adresse IP via DHCP**, avec l’option 43 si configurée.
2. **Ils découvrent le WLC** grâce à l’option 43, DNS, ou broadcast.
3. **Un tunnel CAPWAP** est établi pour la gestion et le trafic utilisateur.

Très bonne question ! Cela dépend **de l’ordre de l’encapsulation** et **de la configuration IPsec**.

Dans un scénario classique **GRE over IPsec** (GRE d'abord, IPsec ensuite), l’ACL pour IPsec **ne voit pas le paquet d’origine encapsulé dans GRE**, mais uniquement **le paquet GRE lui-même**, car le GRE a déjà encapsulé le trafic privé.

### Comment ça fonctionne :
1. **GRE encapsule d'abord le trafic privé** :  
   Exemple : le paquet **10.10.10.1 → 10.10.20.1** est encapsulé dans un en-tête GRE, avec des IP source et destination correspondant aux IP publiques **203.0.113.1 → 203.0.113.5**.  

   Le paquet devient :  
   En-tête IP (203.0.113.1 → 203.0.113.5)  
   En-tête GRE  
   Paquet original (10.10.10.1 → 10.10.20.1)

2. **ACL pour IPsec :**  
   L’ACL utilisée pour IPsec **filtre sur les adresses IP publiques (203.0.113.1 → 203.0.113.5)**, et non sur les adresses privées **10.10.10.0/24 → 10.10.20.0/24**, car ces dernières sont invisibles à ce stade.

   Exemple d’ACL :  
   access-list 101 permit gre host 203.0.113.1 host 203.0.113.5

3. **IPsec chiffre le paquet GRE** :  
   L’ACL correspond au trafic GRE identifié (par l’en-tête IP et GRE), et IPsec encapsule et chiffre tout le paquet GRE, créant un paquet ESP sécurisé.

### Conclusion :
- **Si le paquet est déjà encapsulé dans GRE**, l’ACL pour IPsec filtre sur les adresses publiques et le protocole GRE, **pas sur les adresses privées d’origine**.  
- **Pour protéger le trafic IP privé (10.10.10.0/24 vers 10.10.20.0/24)**, vous devez configurer **l’ACL au niveau de GRE** pour contrôler quel trafic est autorisé à être encapsulé dans le tunnel GRE, **puis IPsec sécurise le tout**.

En résumé : **l’ACL IPsec correspond à l’en-tête GRE et non au paquet d’origine**. Si vous voulez filtrer les paquets d’origine, il faut le faire en amont, avant l’encapsulation GRE.


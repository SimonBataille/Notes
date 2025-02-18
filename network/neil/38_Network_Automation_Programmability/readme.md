# Principes a retenir

- 3 Niveaux :

1. Programmability
  - utilisation de python ou ansible/terraform pour configurer les appareils en une seules fois
  - communication via SSH (south bond interface)

2. Automation SDN : 
  - architecture SDN, cisco SDA est la solution SDN de cisco pour les LAN/WAN d'entreprise
  - SDA applique les principes du SDN pour automatiser et simplifier la gestion des réseaux locaux
  - Cisco SD-Access est une solution de virtualisation et d’automatisation pour les réseaux LAN/WLAN d’entreprise (campus), basée sur Cisco DNA Center.
  - Cisco DNA Center (anciennement Catalyst Center) gère l’automatisation et la supervision des réseaux LAN/WLAN via SD-Access 
  - Underlay : Réseau physique (connectivité IP classique).
  - Overlay : Réseau virtuel utilisant VXLAN pour créer des segments logiques indépendants.
  - Fabric : Architecture globale qui combine underlay et overlay avec des services SDN (segmentation, automatisation)
  - communication (south bon interface) via restconf
  - Les équipements Cisco (switches Catalyst, routeurs ISR, ASR, etc.) doivent exécuter un service interne ou un démon pour supporter NETCONF et RESTCONF

3. Automation WAN 
  - Pour le SDN sur les réseaux étendus (WAN), Cisco propose Cisco SD-WAN, géré par vManage.
  - vManage cloud est une option courante, surtout pour les réseaux multisites ou les entreprises qui ne veulent pas gérer d’infrastructure locale.
  - Les routeurs SD-WAN ont simplement besoin d’un accès Internet pour se connecter à vManage et recevoir leurs configurations.
  - La gestion est centralisée, mais le trafic réseau ne transite jamais par vManage lui-même

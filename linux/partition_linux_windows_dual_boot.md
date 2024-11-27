# A. Windows : Diskpart

1. Commands 
```
DISKPART> list disk

  Disk ###  Status         Size     Free     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  Disk 0    Online          476 GB      0 B        *

DISKPART> list volume

  Volume ###  Ltr  Label        Fs     Type        Size     Status     Info
  ----------  ---  -----------  -----  ----------  -------  ---------  --------
  Volume 0     C                NTFS   Partition    190 GB  Healthy    Boot
  Volume 1     D   软件           NTFS   Partition    286 GB  Healthy
  Volume 2                      FAT32  Partition    100 MB  Healthy    System

DISKPART> list partition

There is no disk selected to list partitions.
Select a disk and try again.

DISKPART> select disk 0

Disk 0 is now the selected disk.

DISKPART> list partition

  Partition ###  Type              Size     Offset
  -------------  ----------------  -------  -------
  Partition 1    System             100 MB  1024 KB
  Partition 2    Reserved           128 MB   101 MB
  Partition 3    Primary            190 GB   229 MB
  Partition 4    Primary            286 GB   190 GB
```

2. Vocabulaire windows
La partition 4 est formatée en NTFS et est montée dans le systeme d'exploitation avec la lettre 'D:' et le label '软件'.

3. Summary Commands Diskpart Linux
```
Commande	Action
list disk	Lister tous les disques connectés.
select disk X	Sélectionner un disque.
list partition	Lister les partitions sur le disque.
select partition X	Sélectionner une partition.
detail partition	Afficher les détails de la partition.
list volume	Lister les volumes montés.
```

# B. Gestion usb linux
```
  323  lsusb
  324  usbreset --help
  325  usbreset --version
  326  usbreset -h
  327  usbreset
  328  usbreset /dev/bus/usb/001/006
  329  usbreset /dev/bus/usb/001/006 
  330  lsblk
  331  sudo usbreset /dev/bus/usb/001/006 
  332  usbreset
  333  usbreset 001/006
  334  lsblk 
  335  sudo usbreset 001/006
  336  lsblk
  337  ls /sys/bus/usb/devices/
  338  echo 0 | sudo tee /sys/bus/usb/devices/1-6/authorized 
  339  lsblk
  340  echo 1 | sudo tee /sys/bus/usb/devices/1-6/authorized 
  341  lsblk
  342  echo 0 | sudo tee /sys/bus/usb/devices/1-6/authorized 
  343  lsblk
  344  echo 1 | sudo tee /sys/bus/usb/devices/1-6/authorized 
```


# C. Windows : Disk, partition, volume, vdisk

- Un disque représente un support de stockage physique ou virtuel.

    Exemple : un disque dur (HDD), un SSD, une clé USB ou un disque virtuel (vdisk).
    Il peut être identifié sous Windows par des noms comme Disque 0, Disque 1, etc., dans l'outil "Gestion des disques".


- Une partition est une division logique d'un disque. Elle permet de séparer et d'organiser les données sur un disque unique.

    Chaque disque peut être divisé en une ou plusieurs partitions.
    Les partitions sont nécessaires pour installer un système de fichiers comme NTFS, FAT32, etc.
    Types courants de partitions :
        Partition principale : Peut être utilisée pour démarrer un système d'exploitation.
        Partition étendue : Peut contenir plusieurs partitions logiques.
        Partition de récupération : Réservée pour les outils de dépannage du système.


- Un volume est une partition formatée avec un système de fichiers et montée dans le système d'exploitation, généralement avec une lettre de lecteur (C:, D:, etc.).

    Un volume peut être composé de :
        Une seule partition.
        Plusieurs partitions fusionnées avec des fonctionnalités comme spanning ou RAID.
    Les volumes sont ce que l'utilisateur voit principalement dans l'explorateur Windows.


- Un vdisk est un disque virtuel, souvent représenté par un fichier sur un disque physique.

    Windows 10 prend en charge les disques virtuels avec le format VHD (Virtual Hard Disk) ou VHDX (extension pour Hyper-V).
    Les vdisks sont utilisés pour :
        Tester des configurations sans avoir besoin d'un disque physique.
        Déployer des machines virtuelles ou des environnements isolés.


# D. Windows : Disk 0
1. Le Disque SSD (GPT)

Le disque est configuré en table de partition GPT (GUID Partition Table), qui offre plusieurs avantages par rapport au schéma MBR :

    Support des disques de grande taille (> 2 To).
    Possibilité d’avoir un nombre quasi illimité de partitions (contre 4 principales en MBR).
    Des données de partitionnement redondantes pour la fiabilité.


2. Les Partitions

Les partitions sont des segments logiques du disque où différentes données ou fonctions du système sont stockées. Voici la signification des partitions décrites :
Partition 1 : System

    Type : Partition EFI (FAT32).
    Taille : Environ 100 à 500 Mo.
    Rôle : Contient le bootloader UEFI, essentiel pour démarrer le système d'exploitation.
        Les fichiers comme bootmgr.efi et d'autres binaires nécessaires au démarrage s'y trouvent.
    Montée comme un volume (v2) avec le système de fichiers FAT32.

Partition 2 : Reserved

    Type : Partition réservée au système.
    Taille : Environ 16 Mo.
    Rôle : Réservée par Windows pour des fonctionnalités comme la gestion de disque dynamique ou des outils de récupération.
    Non montée en tant que volume (pas visible dans l'explorateur Windows).

Partition 3 : Primary (190 GB)

    Type : Partition principale (NTFS).
    Taille : 190 Go.
    Rôle : C'est la partition principale où est installé Windows.
        Montée comme volume C:, elle contient les fichiers système, le répertoire Windows, Program Files, etc.
        Étiquetée comme "Boot" car le système démarre dessus après le passage par la partition EFI.

Partition 4 : Primary (286 GB)

    Type : Partition principale (NTFS).
    Taille : 286 Go.
    Rôle : Partition pour les données personnelles ou autres fichiers non liés au système.
        Montée comme volume D:, accessible dans l'explorateur Windows.

3. Les Volumes

Un volume est une partition formatée et montée, prête à être utilisée par l'utilisateur. Voici les volumes actifs dans ton cas :

    v0 (C:)
        Système de fichiers : NTFS.
        Taille : 190 Go.
        Rôle : Volume contenant l'OS (partition 3).
    v1 (D:)
        Système de fichiers : NTFS.
        Taille : 286 Go.
        Rôle : Volume pour les données (partition 4).
    v2 (System)
        Système de fichiers : FAT32.
        Taille : Une petite taille (généralement 100-300 Mo).
        Rôle : Contient les fichiers de démarrage UEFI.

4. Relation entre Partitions et Volumes

    Partition 1 → v2 (System) : Utilisée au démarrage pour initialiser l'OS.
    Partition 2 → Pas de volume associé (réservée).
    Partition 3 → v0 (C:) : Volume principal avec Windows.
    Partition 4 → v1 (D:) : Volume secondaire pour les données.

5. Conclusion

Cette configuration est standard pour une installation Windows 10 sur un disque en GPT avec démarrage en UEFI. Les points à retenir :

    Partition 1 (System) est indispensable au démarrage.
    Partition 2 (Reserved) est transparente pour l'utilisateur mais nécessaire au système.
    Les partitions C: et D: sont les espaces que tu utilises directement.


# E. Schema GPT

L'offset de 1024 KB avant le début de la partition P1 correspond à l'espace réservé pour la structure GPT et d'autres métadonnées critiques sur le disque. Voici une explication détaillée de ce qui se trouve avant P1 sur un disque partitionné en GPT :

1. Structure des données avant P1

Sur un disque en schéma GPT, voici ce qui se trouve avant la première partition :
a) MBR protecteur (Secteur 0, 512 octets)

Bien qu’un disque GPT ne soit pas structuré comme un disque MBR classique, le premier secteur du disque contient une table MBR spéciale appelée MBR protecteur.

    Rôle : Empêcher les anciens outils de partitionnement qui ne reconnaissent pas GPT de considérer le disque comme "non partitionné".
    Contenu : Une entrée de partition qui couvre tout le disque (indique que le disque est utilisé).

b) En-tête GPT principal (Secteur 1)

    Rôle : Contient des informations sur le schéma GPT, comme :
        Signature "EFI PART".
        La taille et le nombre maximum d'entrées de la table des partitions.
        L'emplacement de l’en-tête GPT de secours.
    Taille : 512 octets.

c) Table des partitions principale (Secteurs 2 à 33, typiquement)

    Rôle : Contient les descriptions des partitions du disque (comme leur type, leur taille, et leur GUID).
    Taille : Chaque entrée de partition fait 128 octets, et il peut y avoir jusqu'à 128 entrées par défaut. Cela occupe généralement 32 secteurs (16 Ko).

d) Alignement par défaut (Microsoft)

Après la table des partitions GPT, il y a souvent un espace réservé pour aligner la première partition à un offset de 1024 KB (1 Mo).

    Raison : Les disques modernes (SSD ou HDD) utilisent des blocs physiques de 4 Ko. Aligner les partitions sur des multiples de 1 Mo améliore les performances en réduisant les lectures/écritures fragmentées.

2. Récapitulatif des offsets sur ton disque

Sur ton disque SSD, voici comment cela se présente avant la partition P1 (System) :

    0 KB - 512 octets : MBR protecteur.
    512 octets - 1 KB : En-tête GPT principal.
    1 KB - 17 KB : Table des partitions GPT principale.
    17 KB - 1024 KB : Zone d'alignement (padding).
    1024 KB : Début de la partition P1.

3. Pourquoi ce padding de 1024 KB ?

    Performance : Un alignement sur 1 Mo (1024 KB) assure que les partitions sont correctement alignées avec les blocs physiques des disques modernes (4K ou plus).
    Compatibilité : Ce choix d’offset est devenu une norme avec Windows Vista et versions ultérieures pour éviter les problèmes d'alignement des partitions.

4. GPT de secours

Pour fiabiliser les données du disque, GPT inclut une copie de l’en-tête GPT et de la table des partitions principale à la fin du disque.

    En-tête GPT de secours : Dernier secteur.
    Table des partitions de secours : Juste avant l’en-tête de secours.

5. Conclusion

Oui, les données GPT (en-tête et table des partitions) et la zone d'alignement sont situées avant l'offset de 1024 KB où commence ta partition P1. Si tu veux explorer ou vérifier ces données, tu peux utiliser un outil comme gdisk ou parted sur Linux, ou diskpart sous Windows. Besoin de détails sur ces outils ?


# F.Dual-Boot
- Installer Linux en dual-boot sur un disque avec un schéma GPT nécessite de préserver la structure GPT et d'organiser les partitions de manière sûre et efficace. Voici les étapes détaillées pour configurer un dual-boot tout en tenant compte des contraintes (comme la GPT de secours à la fin du disque) :

1. Comprendre l'importance de la GPT de secours

    La GPT de secours est située à la fin du disque, mais elle ne fait pas réellement partie de la dernière partition. Elle est stockée dans le dernier secteur du disque, hors des partitions.
    Formater ou modifier la dernière partition (partition 4) ne supprime pas la GPT de secours si l'opération est correctement réalisée.

2. Objectif : Organiser le disque pour Linux

Tu peux utiliser une partie de l’espace actuel de la partition 4 (D:) pour Linux. Voici une proposition :

    Réduire la taille de la partition D: (partition 4) pour libérer de l’espace non alloué.
    Utiliser cet espace pour créer les partitions nécessaires à Linux :
        Partition root / : (ext4) pour le système Linux.
        Partition swap (facultatif si tu as beaucoup de RAM).
        (Optionnel) Partition /home : pour les données utilisateur Linux.
    Installer un chargeur d’amorçage comme GRUB pour gérer le dual-boot.

Installer Linux en dual-boot sur un disque avec un schéma GPT nécessite de préserver la structure GPT et d'organiser les partitions de manière sûre et efficace. Voici les étapes détaillées pour configurer un dual-boot tout en tenant compte des contraintes (comme la GPT de secours à la fin du disque) :
1. Comprendre l'importance de la GPT de secours

    La GPT de secours est située à la fin du disque, mais elle ne fait pas réellement partie de la dernière partition. Elle est stockée dans le dernier secteur du disque, hors des partitions.
    Formater ou modifier la dernière partition (partition 4) ne supprime pas la GPT de secours si l'opération est correctement réalisée.

2. Objectif : Organiser le disque pour Linux

Tu peux utiliser une partie de l’espace actuel de la partition 4 (D:) pour Linux. Voici une proposition :

    Réduire la taille de la partition D: (partition 4) pour libérer de l’espace non alloué.
    Utiliser cet espace pour créer les partitions nécessaires à Linux :
        Partition root / : (ext4) pour le système Linux.
        Partition swap (facultatif si tu as beaucoup de RAM).
        (Optionnel) Partition /home : pour les données utilisateur Linux.
    Installer un chargeur d’amorçage comme GRUB pour gérer le dual-boot.

3. Étapes pour partitionner ton disque
A. Réduire la partition D:

    Ouvrir la Gestion des disques sous Windows :
        Appuie sur Win + R, tape diskmgmt.msc et valide.
    Clic droit sur la partition D (286 Go), puis Réduire le volume.
    Libère un espace suffisant pour Linux :
        50-100 Go est un bon choix pour une utilisation standard.
    Tu obtiens un espace non alloué (non formaté) après D.

B. Installer Linux et créer des partitions :

    Démarre depuis une clé USB Linux live (ex. Ubuntu, Fedora).
    Lors de l'installation :
        Choisis "Utiliser un espace disque existant" ou une option similaire.
        Dans l’espace non alloué, crée :
            Une partition ext4 (minimum 20-30 Go) pour / (racine).
            Une partition swap (2 à 4 Go si tu as peu de RAM ou besoin d'hibernation).
            (Optionnel) Une partition ext4 pour /home si tu souhaites séparer tes données utilisateur.
    Installe GRUB sur la partition EFI existante (Partition 1).

4. Assurer la compatibilité avec Windows

    Partition EFI (P1) : Windows et Linux partagent la même partition EFI (FAT32). GRUB y sera ajouté pour permettre le choix du système au démarrage.
    Windows Bootloader intact : GRUB détecte automatiquement Windows et l'ajoute à son menu.

5. Exemple d'organisation finale du disque
Partition	Type	Taille	Utilisation
P1	FAT32	100-500 MB	Partition EFI (démarrage Windows et Linux).
P2	Reserved	16 MB	Réservée au système Windows.
P3	NTFS	190 GB	Partition Windows (C:).
P4 (modif)	NTFS	186 GB	Partition D: réduite pour données Windows.
P5	ext4	30-50 GB	Partition / pour Linux.
P6	swap	2-4 GB	Partition swap (facultatif).
P7	ext4	20-50+ GB	Partition /home pour Linux (facultatif).

6. Précautions

    Sauvegarde tes données : Avant de redimensionner ou de modifier les partitions.
    Désactive le démarrage rapide de Windows :
        Cela évite des problèmes d'accès aux partitions NTFS depuis Linux.
        Va dans Panneau de configuration > Options d’alimentation > Choisir l’action des boutons d'alimentation et désactive "Activer le démarrage rapide".
    Test des partitions : Une fois le partitionnement effectué, assure-toi que Windows et Linux démarrent correctement.

7. Dual-boot opérationnel

Au démarrage, GRUB te permettra de choisir entre Linux et Windows. Si des questions subsistent (par exemple, pour installer GRUB ou configurer le partitionnement), fais-moi signe !


# G. GRUB
- Excellente question ! Le BIOS (ou plus précisément l'UEFI dans ton cas, étant donné que tu utilises un disque GPT) décide quel chargeur d'amorçage (comme GRUB ou le bootloader Windows) doit être lancé en fonction de l'entrée de démarrage UEFI. Voici comment cela fonctionne en détail :

1. Le rôle de l'UEFI dans le démarrage

UEFI remplace l'ancien BIOS traditionnel et fonctionne différemment :

    Chaque système d'exploitation ou chargeur d'amorçage installe un fichier exécutable sur la partition EFI (P1 dans ton cas), généralement dans un répertoire spécifique.
    UEFI utilise une table appelée NVRAM (Non-Volatile RAM) pour enregistrer les entrées de démarrage. Chaque entrée pointe vers un fichier exécutable EFI sur la partition EFI.

Excellente question ! Le BIOS (ou plus précisément l'UEFI dans ton cas, étant donné que tu utilises un disque GPT) décide quel chargeur d'amorçage (comme GRUB ou le bootloader Windows) doit être lancé en fonction de l'entrée de démarrage UEFI. Voici comment cela fonctionne en détail :
1. Le rôle de l'UEFI dans le démarrage

UEFI remplace l'ancien BIOS traditionnel et fonctionne différemment :

    Chaque système d'exploitation ou chargeur d'amorçage installe un fichier exécutable sur la partition EFI (P1 dans ton cas), généralement dans un répertoire spécifique.
    UEFI utilise une table appelée NVRAM (Non-Volatile RAM) pour enregistrer les entrées de démarrage. Chaque entrée pointe vers un fichier exécutable EFI sur la partition EFI.

2. Installation de GRUB

Lorsque tu installes Linux et choisis de placer GRUB sur la partition EFI, voici ce qui se passe :

    GRUB crée un répertoire dans la partition EFI, généralement nommé /EFI/<distribution> (par exemple, /EFI/ubuntu/ ou /EFI/fedora/).
    GRUB installe son exécutable principal, nommé grubx64.efi, dans ce répertoire.
    Une entrée de démarrage UEFI pour GRUB est ajoutée à la table NVRAM, pointant vers ce fichier.Excellente question ! Le BIOS (ou plus précisément l'UEFI dans ton cas, étant donné que tu utilises un disque GPT) décide quel chargeur d'amorçage (comme GRUB ou le bootloader Windows) doit être lancé en fonction de l'entrée de démarrage UEFI. Voici comment cela fonctionne en détail :
1. Le rôle de l'UEFI dans le démarrage

UEFI remplace l'ancien BIOS traditionnel et fonctionne différemment :

    Chaque système d'exploitation ou chargeur d'amorçage installe un fichier exécutable sur la partition EFI (P1 dans ton cas), généralement dans un répertoire spécifique.
    UEFI utilise une table appelée NVRAM (Non-Volatile RAM) pour enregistrer les entrées de démarrage. Chaque entrée pointe vers un fichier exécutable EFI sur la partition EFI.

2. Installation de GRUB

Lorsque tu installes Linux et choisis de placer GRUB sur la partition EFI, voici ce qui se passe :

    GRUB crée un répertoire dans la partition EFI, généralement nommé /EFI/<distribution> (par exemple, /EFI/ubuntu/ ou /EFI/fedora/).
    GRUB installe son exécutable principal, nommé grubx64.efi, dans ce répertoire.
    Une entrée de démarrage UEFI pour GRUB est ajoutée à la table NVRAM, pointant vers ce fichier.

3. Priorité de démarrage

Le BIOS/UEFI détermine quel chargeur d’amorçage utiliser en fonction de l’ordre des entrées de démarrage dans NVRAM. Cet ordre peut être configuré :

    Lors de l'installation de GRUB, il est souvent automatiquement défini comme prioritaire.
    Si Windows est toujours prioritaire, tu peux changer cela manuellement via l'UEFI ou depuis Linux.

Modifier l'ordre des entrées de démarrage :

    Via l'interface UEFI (accès au BIOS/UEFI pendant le démarrage) :
        Cherche les options de démarrage (Boot Order) et place GRUB en haut de la liste.
    Depuis Linux (avec efibootmgr) :
        Utilise l'outil efibootmgr pour gérer les entrées UEFI.
        Commandes utiles :
		sudo efibootmgr          # Liste les entrées de démarrage
		sudo efibootmgr -o XXXX,YYYY  # Change l'ordre des entrées (remplace XXXX et YYYY par les numéros des entrées)

4. Que se passe-t-il après ?

    Si GRUB est prioritaire dans l'ordre UEFI :
        GRUB démarre et affiche un menu qui te permet de choisir Linux ou Windows.
        GRUB inclut une entrée pour démarrer le chargeur Windows (souvent identifié comme "Windows Boot Manager").
    Si Windows Boot Manager est prioritaire :
        Windows démarrera directement, et tu devras modifier l'ordre dans UEFI ou utiliser un outil pour booter sur GRUB.

5. Problème commun : GRUB écrasé par Windows

Après une mise à jour importante de Windows, il peut arriver que l'entrée UEFI de GRUB soit supprimée ou que Windows Boot Manager reprenne la priorité. Voici comment le résoudre :

1.Réactiver GRUB depuis Linux live :
	Démarre avec une clé USB Linux.
        Monte la partition EFI :

		sudo mount /dev/sdX1 /mnt  # Remplace sdX1 par la partition EFI (P1).

	Réinstalle GRUB :

    		sudo grub-install --efi-directory=/mnt
    		sudo update-grub

2.Restaurer GRUB avec efibootmgr :

    	Ajoute l'entrée de GRUB si elle a disparu :

		sudo efibootmgr -c -d /dev/sdX -p 1 -L "GRUB" -l "\EFI\ubuntu\grubx64.efi"

6. Résumé

    GRUB est installé sur la partition EFI (P1) et enregistré comme une entrée UEFI.
    UEFI détermine quel chargeur utiliser en fonction de l’ordre des entrées dans NVRAM.
    Tu peux changer la priorité de démarrage dans l'UEFI ou via Linux avec efibootmgr.


# H. NVRAM
1. Où est la NVRAM ?

La NVRAM (Non-Volatile RAM) est une mémoire intégrée dans la carte mère, indépendante des disques durs. Elle fait partie du microprogramme UEFI et stocke diverses informations, notamment les entrées de démarrage pour charger les systèmes d'exploitation. La NVRAM n'est pas sur le disque, elle est physiquement située dans la puce UEFI de la carte mère.

2. Peut-on "lister" les fichiers dans la NVRAM ?

La NVRAM ne contient pas de "fichiers", mais des entrées de configuration qui pointent vers des fichiers EFI sur la partition EFI (sur le disque). Ces entrées sont accessibles via des outils spécifiques :

Sous Linux :

	Utilise la commande efibootmgr pour lister les entrées de démarrage stockées dans la NVRAM :

		sudo efibootmgr

	La sortie affiche :

    	BootOrder : L'ordre des entrées de démarrage.
    	BootXXXX : Les entrées spécifiques (ex. GRUB, Windows Boot Manager).


Sous Windows :

    	Ouvre une invite de commande en mode administrateur.
    	Utilise l'outil intégré BCDEDIT pour voir les entrées UEFI :

		bcdedit /enum firmware

	Cela listera les entrées configurées dans la NVRAM.


1. Où est la NVRAM ?

La NVRAM (Non-Volatile RAM) est une mémoire intégrée dans la carte mère, indépendante des disques durs. Elle fait partie du microprogramme UEFI et stocke diverses informations, notamment les entrées de démarrage pour charger les systèmes d'exploitation. La NVRAM n'est pas sur le disque, elle est physiquement située dans la puce UEFI de la carte mère.


2. Peut-on "lister" les fichiers dans la NVRAM ?

La NVRAM ne contient pas de "fichiers", mais des entrées de configuration qui pointent vers des fichiers EFI sur la partition EFI (sur le disque). Ces entrées sont accessibles via des outils spécifiques :
Sous Linux :

Utilise la commande efibootmgr pour lister les entrées de démarrage stockées dans la NVRAM :

sudo efibootmgr

La sortie affiche :

    BootOrder : L'ordre des entrées de démarrage.
    BootXXXX : Les entrées spécifiques (ex. GRUB, Windows Boot Manager).

Sous Windows :

    Ouvre une invite de commande en mode administrateur.
    Utilise l'outil intégré BCDEDIT pour voir les entrées UEFI :

    bcdedit /enum firmware

    Cela listera les entrées configurées dans la NVRAM.


3. Accéder et lister les fichiers de la partition EFI

La partition EFI contient les fichiers nécessaires au démarrage des systèmes d'exploitation (GRUB, Windows Boot Manager, etc.). Voici comment y accéder :

3.1. Sous Linux :

    Monte la partition EFI (généralement FAT32) :

sudo mount /dev/sdX1 /mnt

    Remplace /dev/sdX1 par l'identifiant de la partition EFI (par exemple, /dev/nvme0n1p1 ou /dev/sda1).

Explore les fichiers :

ls /mnt/EFI

Tu verras probablement des répertoires comme :

    Microsoft : Contient le Windows Boot Manager.
    ubuntu ou une autre distribution Linux : Contient GRUB (grubx64.efi).

Une fois terminé, démonte la partition :

sudo umount /mnt

3.2.Sous Windows :

    Ouvre l'outil Gestion des disques :
        Appuie sur Win + R, tape diskmgmt.msc, et valide.

    Identifie la partition EFI (elle est de petite taille, ex. 100-500 Mo, et formatée en FAT32).

    Attribue une lettre de lecteur :
        Clic droit sur la partition EFI > Modifier la lettre de lecteur et les chemins > Ajouter > Choisis une lettre.

    Une fois la lettre attribuée (ex. Z:), utilise l'Explorateur de fichiers ou l'invite de commande pour accéder à la partition :

dir Z:\

Explore les fichiers :

    Les fichiers sont organisés dans des répertoires comme EFI\Microsoft ou EFI\Boot.


4. Précautions pour la partition EFI

    Ne modifie pas les fichiers à moins de savoir ce que tu fais, car cela pourrait rendre le système non amorçable.
    Si tu apportes des modifications, conserve une sauvegarde de la partition EFI.


5. Résumé des commandes utiles
Tâche	Windows	Linux
Lister les entrées de la NVRAM	bcdedit /enum firmware	sudo efibootmgr
Accéder à la partition EFI	Attribuer une lettre avec Gestion des disques	sudo mount /dev/sdX1 /mnt
Lister les fichiers dans la partition EFI	dir Z:\ après attribution de lettre	ls /mnt/EFI


# I. Partitionnement de disk 0

Résumé des commandes utiles
Tâche	Windows	Linux
Lister les entrées de la NVRAM	bcdedit /enum firmware	sudo efibootmgr
Accéder à la partition EFI	Attribuer une lettre avec Gestion des disques	sudo mount /dev/sdX1 /mnt
Lister les fichiers dans la partition EFI	dir Z:\ après attribution de lettre	ls /mnt/EFI

1. Répartition de l’espace disque entre Windows et Linux
Scénario de base :

Tu disposes d’un disque SSD de 512 Go.
Partition	Utilisation	Taille recommandée
Windows (C:)	Système Windows et logiciels	80-100 Go
D:	Partage de fichiers entre OS	50-100 Go
Linux /	Système Linux (OS et logiciels)	30-40 Go
Linux /home	Données personnelles Linux	150-200 Go
Linux swap	Mémoire virtuelle (facultatif)	2-4 Go

2. Justification de la répartition
Pour Windows :

    C: (80-100 Go) :
        Suffisant pour Windows 10/11 (qui occupe environ 20 Go) et quelques logiciels ou jeux légers.
        Si tu ne prévois pas d'utiliser Windows fréquemment ou pour des tâches gourmandes, cette taille est idéale.

    D: (50-100 Go) :
        Cette partition peut servir de zone de partage entre Linux et Windows.
        Formate-la en NTFS (compatible en lecture/écriture avec les deux systèmes).
        Si tu n’as pas besoin de beaucoup de données partagées, 50 Go suffisent.

Pour Linux :

    / (30-40 Go) :
        Contient le système Linux et les logiciels.
        30 Go est généralement suffisant pour un usage classique (système + logiciels courants).
        Si tu utilises des logiciels volumineux (ex. IDE, outils de virtualisation), opte pour 40 Go.

    /home (150-200 Go) :
        Contient tes fichiers personnels et tes configurations utilisateur.
        La taille dépend de la quantité de données que tu stockes sous Linux (projets, médias, etc.).
        C'est ici que tu devrais allouer le plus d'espace si Linux est ton OS principal.

    Swap (2-4 Go) :
        Si tu disposes de suffisamment de RAM (ex. 16 Go ou plus), la partition swap est rarement utilisée, sauf pour l'hibernation.
        2-4 Go suffisent dans la plupart des cas.

3. Répartition finale sur ton disque de 512 Go
Partition	Taille	Format	Description
Partition EFI	100-500 Mo	FAT32	Partition existante pour le démarrage (GRUB et Windows Boot Manager).
Windows (C:)	100 Go	NTFS	Système Windows et logiciels.
D:	50 Go	NTFS	Zone de partage entre Windows et Linux.
Linux /	40 Go	ext4	Système Linux et logiciels.
Linux /home	200 Go	ext4	Données personnelles Linux.
Swap	2-4 Go	swap	Mémoire virtuelle Linux.


4. Étapes pour configurer le dual-boot

    Préparer l'espace sous Windows :
        Réduis les partitions actuelles depuis la Gestion des disques (diskmgmt.msc) pour libérer de l’espace non alloué.
        Réduis D: (ou supprime-la si nécessaire), puis libère environ 250-300 Go pour Linux.

    Installer Linux :
        Lors de l’installation, choisis Partitionnement manuel pour créer les partitions suivantes dans l’espace non alloué :
            / : 40 Go, format ext4.
            /home : 200 Go, format ext4.
            Swap : 2-4 Go.

    Installer GRUB :
        Installe GRUB sur la partition EFI existante. GRUB détectera automatiquement Windows et ajoutera une entrée pour son démarrage.

    Configurer le partage :
        Utilise la partition D: pour stocker les fichiers partagés.
        Monte automatiquement cette partition dans Linux en modifiant le fichier /etc/fstab (optionnel).

5. Pourquoi conserver une partition D pour le partage ?

    Avantage pratique : Si tu utilises Linux la majorité du temps, la partition D: permet un accès rapide aux fichiers partagés sans redémarrer sous Windows.
    Compatibilité NTFS : Linux gère bien NTFS pour le partage de fichiers.

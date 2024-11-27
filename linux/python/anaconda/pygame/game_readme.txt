python -m idlelib


conda search pygame
conda config --add channels conda-forge : pygame on channel conda-forge

conda env export > environment.yml

conda install pygame


conda install -c conda-forge pygame
conda install -c conda-forge alsa-lib

python -m pygame.examples.aliens


'''
name: my_env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.12
  - pygame
  # d'autres dépendances peuvent être ajoutées ici

'''


Résumé des commandes :

    Désactiver base au démarrage : conda config --set auto_activate_base false
    Activer manuellement base : conda activate base
    Réactiver base par défaut : conda config --set auto_activate_base true


Si conda n'est plus dans le path et que .bashrc n'est pas modifié
	source ~/anaconda3/etc/profile.d/conda.sh
	conda activate base


Isolation
L’isolation dans Conda repose sur des mécanismes simples (chemins, variables d’environnement) et ne fournit pas de sandbox système complète comme Docker. Si vous avez besoin d’une isolation stricte, Docker ou d’autres technologies de conteneurisation sont plus adaptés.

Résumé : Isolation Conda vs Docker
Caractéristique	Conda	Docker
Fichiers	Installé dans un répertoire dédié	Installé dans un système de fichiers isolé (UnionFS)
Réseau	Accès complet au réseau système	Réseau isolé par défaut
Processus	Aucune isolation spécifique	Isolation via namespaces (PID, UTS, etc.)
Ressources (CPU, RAM)	Partage total des ressources système	Limité par cgroups
Portabilité	Doit être configuré sur chaque machine	Conteneur portable avec l’environnement
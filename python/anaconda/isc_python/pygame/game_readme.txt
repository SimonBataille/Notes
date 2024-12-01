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


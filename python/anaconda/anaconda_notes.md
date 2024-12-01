# 1. Notes about anaconda on linux systems

# 2. Docs
https://docs.conda.io/projects/conda/en/latest/user-guide

# Create python project
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/creating-projects.html

# 3. Create Conda project for jupyter-lab
```
mkdir example
cd example

touch environment.yaml
'''yaml
name: example
channels:
  - defaults
dependencies:
  - python
  - ipykernel
  - numpy
  - matplotlib
  - jupyterlab
  - dask
  - pandas
  - hvplot
  - conda-forge::condastats
'''

conda env create --file environment.yaml
conda activate example
jupyter-lab
jupyter kernelspec list
    => Kernels are processes that run independently and interact with JupyterLab. ipykernel provides the IPython kernel for Jupyter, which provides an interactive Python development environment. Kernels in JupyterLab allow the use of different Python versions and virtual environments. By default, one or more kernels will exist when you log into JupyterLab running on Posit Workbench.
cat /home/simon/anaconda3/envs/example/share/jupyter/kernels/python3/kernel.json
conda env update --file environment.yaml
conda activate example
python -m ipykernel install --user --name=example --display-name "Python (example)"
    => (example) simon@simon-HP-EliteBook-735-G6:~/Documents/Geek/Python/Anaconda/example$ python -m ipykernel install --user --name=example --display-name "Python (example)"
Installed kernelspec example in /home/simon/.local/share/jupyter/kernels/example
```

# 4. Manage Conda CLI
```
conda --version
conda env list
conda create --name example
conda env list
conda activate example
conda list
conda env list
conda install jupyterlab dask pandas hvplot
conda install -c conda-forge condastats
jupyter-lab
conda deactivate
conda activate example
jupyter-lab
conda deactivate
conda activate example
clear
conda install ipykernel
conda install notebook
python -m ipykernel install --user --name=example
jupyter notebook
conda deactivate
anaconda-navigator 
conda deactivate
history
anaconda-navigator 
anaconda-navigator
conda activate
anaconda-navigator 
sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"
conda activate example
history
jupyter notebook
conda deactivate
jupyter notebook list
jupyter notebook stop 8888
jupyter notebook stop 8889
history
```

# 5. Kernel
- Un kernel est un processus qui exécute le code que vous écrivez dans Jupyter Notebook ou Jupyter Lab. Il agit comme un moteur d'exécution pour une langue donnée, généralement Python dans votre cas.

- Voici comment le kernel et Jupyter Lab interagissent :

1. Rôle du kernel

    Exécution du code : Lorsque vous écrivez du code dans une cellule Jupyter, ce code est envoyé au kernel pour être exécuté. Le kernel renvoie ensuite les résultats, qui sont affichés dans Jupyter.
    Contexte d'exécution : Le kernel conserve l'état de votre session (variables, fonctions définies, bibliothèques importées, etc.). Tant que le kernel est actif, vous pouvez accéder à ces informations.

2. Types de kernels

Chaque environnement ou langage peut avoir son propre kernel. Par exemple :

    python3 : Kernel Python standard.
    example : Un kernel Python pour votre environnement example créé avec conda.
    R : Si vous installez un kernel pour le langage R.
    Julia : Pour Julia, etc.

Le kernel associé à l'environnement conda example se trouve ici dans votre cas :

/home/simon/anaconda3/envs/example/share/jupyter/kernels/python3

Cela signifie que le kernel Python 3 utilisé est bien associé à l'environnement example

3. Jupyter Lab et les kernels

    Jupyter Lab est une interface utilisateur graphique. Elle vous permet de créer et d'exécuter des notebooks, de visualiser des résultats, et de travailler dans différents langages via leurs kernels.
    Lorsque vous démarrez Jupyter Lab, il détecte tous les kernels disponibles et vous permet de choisir celui que vous voulez utiliser pour un notebook donné.

4. Lien avec votre configuration

Dans votre cas :

    L'environnement example contient Python et plusieurs bibliothèques comme numpy, matplotlib, etc.
    Jupyter Lab a détecté cet environnement et lui a associé le kernel Python 3.
    Lorsque vous ouvrez un notebook dans Jupyter Lab, assurez-vous de sélectionner ce kernel (Python 3 (example)) dans le menu Kernel > Change Kernel.

5. Pourquoi un kernel spécifique par environnement ?

    Isolation : Chaque environnement conda peut avoir des versions différentes de Python ou des bibliothèques. Avoir un kernel spécifique à chaque environnement garantit que le code utilise les versions correctes.
    Flexibilité : Vous pouvez travailler sur plusieurs projets avec des dépendances différentes sans conflit.

Si vous souhaitez ajouter ou tester d'autres kernels, vous pouvez explorer des kernels pour R, Julia ou même des langages comme C++ avec xeus.


# 6. Default Kernel

- Jupyter Lab peut détecter et utiliser un kernel même si vous n'avez pas explicitement installé ipykernel ou exécuté la commande python -m ipykernel install. Voici pourquoi cela fonctionne quand même :

1. Jupyter utilise un kernel Python global par défaut

Lorsque vous installez Jupyter (via conda ou pip), il installe généralement le package ipykernel dans l'environnement de base (base). Ce kernel Python global est automatiquement disponible pour tous les environnements qui partagent la même installation de Jupyter.

2. Environnements conda et Jupyter

Les environnements conda sont conçus pour partager certains outils installés dans l'environnement base. Voici ce qui se passe :

    Jupyter détecte automatiquement l'interpréteur Python de l'environnement example via le fichier kernelspec généré par conda lors de la création de l'environnement.
    Si vous démarrez Jupyter Lab depuis un environnement conda (ou globalement), il est capable d'utiliser ce lien implicite sans installer explicitement ipykernel dans l'environnement.

C'est pourquoi, même sans exécuter python -m ipykernel install, le kernel apparaît comme disponible.

3. Fichier kernelspec généré par conda

Lorsqu'un environnement conda est créé, un fichier de configuration pour le kernel peut être généré automatiquement si Jupyter est installé dans l'environnement base. Ce fichier est situé dans :
```
/home/simon/anaconda3/envs/example/share/jupyter/kernels/python3/kernel.json
```

Ce fichier contient quelque chose comme ceci :
```
{
  "argv": [
    "/home/simon/anaconda3/envs/example/bin/python",
    "-m",
    "ipykernel_launcher",
    "-f",
    "{connection_file}"
  ],
  "display_name": "Python 3",
  "language": "python"
}
```

Cela suffit pour que Jupyter détecte l'environnement comme un kernel utilisable, même si ipykernel n'est pas explicitement dans les dépendances.

4. ipykernel déjà présent implicitement

Bien que vous n'ayez pas ajouté ipykernel dans les dépendances de votre fichier environment.yaml, il est probable qu'il ait été installé indirectement comme dépendance d'un autre package (par exemple, jupyterlab ou notebook).

5. Pourquoi ajouter explicitement ipykernel ou utiliser la commande python -m ipykernel install ?

Même si tout fonctionne dans votre cas, il peut être utile de :

    Installer explicitement ipykernel : Pour garantir que l'environnement example est autonome et n'a pas besoin de dépendances globales.
    Utiliser python -m ipykernel install : Pour personnaliser le nom du kernel (comme Python (example)) ou pour créer un kernel clair et spécifique à un environnement.

6. Conclusion

Jupyter Lab fonctionne avec votre environnement grâce à des mécanismes implicites et des partages entre l'environnement base et les autres environnements conda. Cependant, pour une meilleure clarté et portabilité, il est souvent recommandé d'installer explicitement ipykernel et de configurer les kernels de manière spécifique.

# 7. Activation Conda Environment
## 7.1. Résumé des commandes :

    Désactiver base au démarrage : conda config --set auto_activate_base false
    Activer manuellement base : conda activate base
    Réactiver base par défaut : conda config --set auto_activate_base true

## 7.2. Activation (base)
Si conda n'est plus dans le path et que .bashrc n'est pas modifié
```bash
	source ~/anaconda3/etc/profile.d/conda.sh
	conda activate base
```

# 8. Isolation
- L’isolation dans Conda repose sur des mécanismes simples (chemins, variables d’environnement) et ne fournit pas de sandbox système complète comme Docker. Si vous avez besoin d’une isolation stricte, Docker ou d’autres technologies de conteneurisation sont plus adaptés.

## Résumé : Isolation Conda vs Docker
|Caractéristique | Conda | Docker
|--|--|--|
Fichiers | Installé dans un répertoire dédié | Installé dans un système de fichiers isolé (UnionFS)
Réseau | Accès complet au réseau système | Réseau isolé par défaut
Processus | Aucune isolation spécifique	| Isolation via namespaces (PID, UTS, etc.)
Ressources (CPU, RAM) | Partage total des ressources système | Limité par cgroups
Portabilité	| Doit être configuré sur chaque machine | Conteneur portable avec l’environnement


# Fonctionnement de l'interaction entre Python et NumPy (fichiers .so)

Quand Python utilise **NumPy**, il charge des fichiers `.so` (bibliothèques dynamiques) qui contiennent le code natif optimisé pour effectuer les calculs. Cependant, **ce code ne s'exécute pas indépendamment de Python**. Voici une explication détaillée :

---

## 1. Chargement des fichiers `.so`
- Lorsque vous importez NumPy en Python :
  ```python
  import numpy as np
  ```
  Python utilise le mécanisme de **bibliothèque dynamique** pour charger les modules natifs de NumPy. Ces modules sont généralement des fichiers `.so` (sous Linux) ou `.dll` (sous Windows).

- Ces fichiers `.so` incluent :
  - Le code natif écrit en **C** ou **Cython** (un sur-ensemble de Python compilé en C).
  - Des bibliothèques mathématiques optimisées comme **BLAS**, **LAPACK**, ou **OpenBLAS**.

- Python utilise **le chargeur dynamique (`ld.so`)** pour lier et charger ces bibliothèques dans l'espace mémoire du processus Python en cours d'exécution.

---

## 2. Le code `.so` ne crée pas de nouveau processus
- Le code natif contenu dans les fichiers `.so` **s'exécute dans le même processus que l'interpréteur Python**.
- Il n’y a pas besoin de communication entre processus, car tout se passe dans un seul espace mémoire.

---

## 3. NumPy ne s'exécute pas de manière indépendante
- NumPy n'est pas un processus distinct. Ses calculs se déroulent dans le même espace mémoire que Python :
  - Python appelle une fonction NumPy (par exemple, `np.sum()`).
  - Cette fonction transmet les données au code natif dans les bibliothèques `.so`.
  - Le calcul est effectué directement dans le contexte du processus Python.

- Cependant, NumPy peut tirer parti de **bibliothèques parallèles** ou de **threads natifs** (par exemple, via OpenMP) pour accélérer les calculs. Ces threads sont créés et gérés dans le contexte du processus Python.

---

## 4. Exemple de fichiers `.so` chargés par NumPy
Vous pouvez voir les fichiers `.so` que NumPy charge en exécutant un script Python avec **strace** (outil pour suivre les appels système) :
```bash
strace -e open python -c "import numpy"
```

Sortie typique (simplifiée) :
```
open("/usr/lib/python3.9/site-packages/numpy/core/_multiarray_umath.cpython-39-x86_64-linux-gnu.so", O_RDONLY) = 3
open("/usr/lib/libblas.so.3", O_RDONLY) = 4
```

---

## 5. Interaction entre Python et NumPy
- Python transmet les données (par exemple, des tableaux NumPy) au code natif via des **buffers mémoire** ou des **pointeurs**.
- NumPy effectue les calculs directement sur ces données, souvent sans duplication :
  - Les tableaux NumPy utilisent un **tampon mémoire** qui peut être manipulé par le code natif sans copie.
  - Le code `.so` lit et modifie directement ce tampon.

---

## 6. Exemple simple : Appel de `numpy.sum()`
Lorsqu'on exécute :
```python
import numpy as np
arr = np.array([1, 2, 3, 4])
result = np.sum(arr)
```

Voici ce qui se passe :
1. **Chargement de la bibliothèque** :
   - Lors de `import numpy`, les fichiers `.so` sont chargés dans le processus Python.
2. **Appel Python vers NumPy** :
   - L'appel `np.sum(arr)` transmet les données de `arr` à une fonction native dans le fichier `.so`.
3. **Calcul natif** :
   - Le code natif (écrit en C) effectue la somme directement sur les données du tableau.
4. **Retour du résultat** :
   - Le résultat (un scalaire Python) est retourné à l'interpréteur Python.

---

## 7. Pourquoi charger des `.so` ?
Les fichiers `.so` permettent à NumPy d'être :
- **Rapide** :
  - Les calculs lourds sont effectués en C, bien plus rapide que Python pur.
- **Efficace** :
  - Les données sont manipulées directement sans copies inutiles.
- **Interopérable** :
  - NumPy peut tirer parti de bibliothèques tierces optimisées comme BLAS ou LAPACK.

---

## Résumé
- **Oui**, lorsque Python utilise NumPy, il charge des fichiers `.so` pour exécuter les calculs natifs.
- **Non**, le code NumPy ne s'exécute pas dans un processus distinct. Il s'exécute dans le même processus que Python.
- Python et NumPy partagent les données via des tampons mémoire et des pointeurs, sans duplication inutile.

Si vous souhaitez approfondir un aspect spécifique, n'hésitez pas à demander !

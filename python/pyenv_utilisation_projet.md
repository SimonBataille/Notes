
# Utilisation de `pyenv` pour Choisir une Version de Python pour un Projet

## Configuration Actuelle
Dans ta configuration, où tu exécutes manuellement les commandes :
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
Toutes les modifications faites par `pyenv` s'appliquent uniquement à la session de terminal en cours.

---

## 1. Choisir une Version de Python pour un Projet

### a) Configurer une Version Locale pour un Projet
La configuration locale associe une version de Python à un répertoire particulier. Cela s'applique uniquement lorsque tu travailles dans ce répertoire.

1. Place-toi dans le répertoire du projet :
   ```bash
   cd /chemin/vers/mon_projet
   ```

2. Configure la version de Python locale :
   ```bash
   pyenv local 3.9.7
   ```

3. Vérifie que la bonne version est utilisée :
   ```bash
   python --version
   ```

**Ce que cela fait :**
- `pyenv` crée un fichier caché `.python-version` dans le répertoire du projet.
- Lorsqu'un shell actif est dans ce répertoire, `pyenv` utilise automatiquement la version spécifiée.

### b) Configurer une Version Globale
Si tu veux définir une version par défaut pour toutes tes sessions, utilise la commande globale :
```bash
pyenv global 3.9.7
```

Cela affecte toutes les sessions utilisant `pyenv`, mais **dans ton cas**, cela ne s'applique que tant que tu as activé `pyenv` dans ton shell.

---

## 2. Revenir à la Version Système de Python
Si tu veux revenir à la version de Python fournie par ton système, utilise la commande :
```bash
pyenv global system
```

Cela force `pyenv` à désactiver sa gestion de Python, laissant le shell utiliser la version Python globale installée sur ton système.

- Pour un projet spécifique (local), utilise :
  ```bash
  pyenv local system
  ```

---

## 3. Vérifier Quelle Version est Active
Pour vérifier la version de Python actuellement utilisée dans ton shell, exécute :
```bash
pyenv version
```
Cela affichera la version active (par exemple, `3.9.7`) et son origine (globale ou locale).

---

## 4. Ton Cas : `pyenv` Modifie Uniquement le Shell Actuel
Oui, avec ta configuration où tu exécutes manuellement :
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
Toutes les modifications faites par `pyenv` sont limitées à la session shell active. Lorsque tu fermes ce terminal, `pyenv` ne laisse aucun changement permanent sur ton système.

---

## Résumé des Commandes Importantes

1. **Lister les versions disponibles :**
   ```bash
   pyenv versions
   ```

2. **Installer une nouvelle version de Python :**
   ```bash
   pyenv install 3.10.7
   ```

3. **Définir une version locale :**
   ```bash
   pyenv local 3.10.7
   ```

4. **Définir une version globale :**
   ```bash
   pyenv global 3.10.7
   ```

5. **Revenir à la version système :**
   ```bash
   pyenv global system
   ```

6. **Vérifier la version active :**
   ```bash
   pyenv version
   ```

Avec ces commandes, tu peux gérer facilement les versions de Python pour tes projets sans toucher à ta configuration système. 🎉

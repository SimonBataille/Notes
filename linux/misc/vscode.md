# Sync
- Sync : lors de la première authentification Vscode stocks les infos d'authentification outlook pour se connecter au cloud, idéalement il faut que les passwords soient stockés dans un fichier crypté keepassXc

# Sync mode basic
- Sync mode basic : les passwords et les jetons de outlook sont stockés dans
```
grep -ri "auth" ~/.config/Code/User/
grep: /home/simon/.config/Code/User/workspaceStorage/640b63b379af42e60edb28c8e30c0fde/state.vscdb.backup : fichiers binaires correspondent
grep: /home/simon/.config/Code/User/workspaceStorage/640b63b379af42e60edb28c8e30c0fde/state.vscdb : fichiers binaires correspondent
grep: /home/simon/.config/Code/User/workspaceStorage/1729149801194/state.vscdb.backup : fichiers binaires correspondent
grep: /home/simon/.config/Code/User/workspaceStorage/1729149801194/state.vscdb : fichiers binaires correspondent
grep: /home/simon/.config/Code/User/globalStorage/state.vscdb.backup : fichiers binaires correspondent
grep: /home/simon/.config/Code/User/globalStorage/state.vscdb : fichiers binaires correspondent
```

# Reinit vscode 
- Réinit VsCode sans suppprimer les librairies : 

      rm -rf ~/.config/Code/

# Extensions
- Le debbugger python est installé dans les extensions

            (.venv) (base) simon@simon-HP-EliteBook-735-G6:~/Documents/Geek/Python/Vscode$  cd /home/simon/Documents/Geek/Python/Vscode ; /usr/bin/env /home/simon/Documents/Geek/Python/Vscode/.venv/bin/python /home/simon/.vscode/extensions/ms-python.debugpy-2024.12.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher 54091 -- /home/simon/Documents/Geek/Python/Vscode/main.py 

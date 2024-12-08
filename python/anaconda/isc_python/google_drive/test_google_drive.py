'''
1. Inscription google cloud
2. Creation projet : 'My first project'
3. Chercher et activer l'option drive api
4. - Creation d'identifiants pour permettre au script d'acceder a l'api drive de google
   - /!\ ne permet pas d'acceder au drive de qqun (credentials)
   - Selectionner 'Donnees utilisateurs' : le client final se connecte avec ses propres identifiants pour
     acceder a son propre drive
5. Ecran de consentement : s'enregister comme utilisateur test
6. conda install conda-forge::pydrive2
'''

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


# on s'authentifie en creant un serveur local
# pour recuperer les credentials de l'api google drive
# on enregistre les credentials dans un fichier
# /!\ les credentials du cloud sont disponibles dans client_secrets.json
gauth = GoogleAuth()
#gauth.LocalWebserverAuth()
#gauth.SaveCredentialsFile('gdrive_credentials.json')

# Une fois les credentials de drive recuperes
# on peut les charger 
gauth.LoadCredentialsFile('gdrive_credentials.json')


# On accede au drive pour lister les fichiers a la racine
drive = GoogleDrive(gauth)
liste = drive.ListFile({'q' : "'root' in parents and trashed=false"}).GetList()
for fichier in liste:
    print(fichier['title'], '->', fichier['id'])


# On pousse un fichier sur le drive
# fichier_local = 'test.png'
# fichier_drive = drive.CreateFile({'title': 'test2.png'})
# fichier_drive.SetContentFile(fichier_local)
# fichier_drive.Upload()


# On recupere un fichier depuis le drive via l'id du fichier
fichier_id = '1BBS28bYEWZWc6tjtdJGvEZGASVtlJdX7'
fichier_from_drive = drive.CreateFile({'id' : fichier_id})
fichier_from_drive.GetContentFile('test2.png')


'''
google cloud est le conteneur des api google. Pour acceder aux api il faut passer par google cloud, creer un projet qui exposera les api via une application que l'on definie. C'est cette application qui sera appelee par les applications utilisatrices. 

En résumé :
Google Cloud est l'endroit où vous créez et gérez les projets qui exposent les API Google.
Vous créez un projet et activez les API Google (par exemple, Google Drive) dans ce projet.
Vous définissez une application d'authentification OAuth qui permettra à l'utilisateur de se connecter à son compte Google et d'autoriser l'accès à ses données.
L'application utilisatrice (comme votre script Python ou une application mobile) utilise ces credentials OAuth pour accéder aux services Google via les API.

Conclusion :
Oui, Google Cloud agit comme le conteneur pour les API, et c'est via un projet Google Cloud que vous exposez ces API et gérez l'accès à vos données via des applications.
'''

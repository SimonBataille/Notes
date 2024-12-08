# Etapes
1. Creer ou selectionner un projet 'My First Project'
2. Activer l'api 'Kubernetes Engine API'
3. Acceder au 'Kubernetes Engine'
4. Creer un cluster 'Autopilot'
5. Ouvrir le cloud shell pour acceder au shell de la VM linux
6. Cloner le code de l'application a deployer sur le cluster : git clone `https://github.com/GoogleCloudPlatform/microservices-demo.git`
7. Ouvrez le répertoire contenant l'exemple de code dans l'éditeur Cloud Shell (ide graphique ressemble a vscode) : `cloudshell workspace microservices-demo`
8. Vous connecter à votre cluster GKE
    - Pour ajouter un cluster GKE, procédez comme suit :
        Dans le menu Affichage, cliquez sur Palette de commandes.
        Saisissez add cluster, puis cliquez sur Ajouter un cluster au fichier KubeConfig.
        Sélectionnez Google Kubernetes Engine.
        Cette opération peut prendre un certain temps.
        Une fois l'opération réalisée, sélectionnez my-autopilot-cluster us-central1.
    - Votre nouveau cluster GKE apparaît dans la section Clusters. 
    - `ls -l ~/.kube/config`
9. Déployer l'application exemple : `kubectl apply -f ./release/kubernetes-manifests.yaml`
10. Consulter une version de démonstration dans votre navigateur : `kubectl get services`
11. Notez l'adresse IP externe du service frontend-external
12. http://104.198.229.51
13. Fermer google cloud shell IDE
14. Supprimer le cluster

# Interaction entre Google Cloud Shell et le cluster Autopilot

## 1. Le cluster Autopilot est instancié sur des VMs dédiées
- Lors de la création de votre cluster Kubernetes (Autopilot), Google Kubernetes Engine (GKE) crée automatiquement des **nœuds Kubernetes**.
- Ces nœuds sont des **VMs gérées** par Google Cloud, utilisées pour exécuter vos applications et vos pods.
- Vous n'avez pas accès direct à ces VMs dans un cluster Autopilot, car GKE gère leur création, leur scalabilité, et leur maintenance.

## 2. La VM éphémère Cloud Shell
- La VM éphémère de **Google Cloud Shell** est indépendante des VMs utilisées par votre cluster Kubernetes.
- Elle est utilisée comme un **client** pour interagir avec les services Google Cloud, y compris votre cluster Kubernetes.
- Cloud Shell fournit un environnement préconfiguré avec des outils comme `kubectl` et `gcloud`, ce qui facilite la gestion de vos projets.

## 3. Le lien entre le cluster et votre VM Cloud Shell
Le lien est établi grâce au fichier **KubeConfig**, qui contient les informations nécessaires pour se connecter à votre cluster Kubernetes.

### a) Clusters
```yaml
clusters:
- cluster:
    server: https://34.72.185.150
  name: gke_erudite-scanner-444011-u6_us-central1_autopilot-cluster-1
```

- Ce champ définit le server, qui est l'adresse publique du plan de contrôle Kubernetes pour votre cluster (34.72.185.150).
- Cette adresse est utilisée par kubectl pour envoyer des commandes au cluster.

### b) Contexts
```yaml
contexts:
- context:
    cluster: gke_erudite-scanner-444011-u6_us-central1_autopilot-cluster-1
    user: gke_erudite-scanner-444011-u6_us-central1_autopilot-cluster-1
```

- Un context relie un cluster spécifique à un utilisateur. Il indique sur quel cluster et avec quels credentials les commandes kubectl doivent être exécutées.

### c) Users
```yaml
users:
- name: gke_erudite-scanner-444011-u6_us-central1_autopilot-cluster-1
  user:
    exec:
      command: gke-gcloud-auth-plugin
      args:
      - --use_application_default_credentials
```
- Le champ user configure les informations d'authentification. Dans ce cas, le plugin gke-gcloud-auth-plugin est utilisé pour récupérer un jeton d'accès OAuth via les credentials de Google Cloud.

### d) Plugin d'authentification
- Le plugin `gke-gcloud-auth-plugin` utilise vos credentials Google Cloud pour accéder au cluster.
- Cloud Shell gère automatiquement ces credentials, car il est lié à votre compte Google Cloud.

## 4. Interaction entre Cloud Shell et le cluster

   1. Authentification :
   - Lorsque vous exécutez une commande `kubectl` depuis Cloud Shell, le plugin `gke-gcloud-auth-plugin` s'authentifie en utilisant vos credentials Google Cloud.

   2. Accès au plan de contrôle :
   - Toutes les commandes `kubectl` passent par l'adresse publique du plan de contrôle Kubernetes (`server` dans KubeConfig).

   3. Interaction avec les nœuds :
   - Le plan de contrôle transmet les requêtes (par exemple, déployer un pod) aux nœuds Kubernetes (VMs) du cluster.

## 5. Résumé

- Autopilot :
 - Il est exécuté sur des VMs dédiées gérées automatiquement par Google Cloud.
 - Ces VMs ne sont pas accessibles directement.
- Cloud Shell :
 - C'est une VM éphémère utilisée comme environnement client pour interagir avec votre cluster.
- Fichier KubeConfig :
 - Il configure l'accès au plan de contrôle Kubernetes via :
   - L'adresse publique du cluster,
   - Les credentials d'authentification,
   - Le contexte du cluster.
- L'infrastructure sous-jacente (comme les nœuds Kubernetes) est gérée automatiquement, vous permettant de vous concentrer sur le déploiement et la gestion des applications.




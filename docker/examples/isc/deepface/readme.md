# Python
`pip install deepface`

`pip install tf-keras`
`ctrl + shift + u` + `2588`

# Models
Downloading...
From: https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5
To: /home/simon/.deepface/weights/vgg_face_weights.h5
`ls ~/.deepface/weights`

# Flow
Le lien entre **TensorFlow**, **tf-keras**, et **DeepFace** peut être clarifié en comprenant le rôle de chaque bibliothèque dans le processus global d'analyse d'images et de vision par ordinateur.

### 1. **TensorFlow**

**TensorFlow** est une bibliothèque open-source développée par Google pour la création et l'entraînement de modèles de machine learning et d'intelligence artificielle (IA). C'est un framework de bas niveau qui offre une grande flexibilité pour travailler avec des réseaux de neurones, mais qui peut aussi être complexe à utiliser directement pour des tâches spécifiques.

TensorFlow fournit des outils et des API pour la création, l'entraînement et l'exécution de modèles d'apprentissage profond, mais son utilisation directe peut être plus difficile si vous souhaitez effectuer des tâches spécifiques telles que la reconnaissance faciale.

### 2. **Keras et tf-keras**

**Keras** est une bibliothèque d'API de haut niveau pour le deep learning. Elle a été initialement développée de manière indépendante, mais a été intégrée dans **TensorFlow** à partir de TensorFlow 2.0, sous le nom de `tf.keras`.

- **Keras** simplifie l'usage de **TensorFlow** en offrant une interface plus intuitive pour définir et entraîner des modèles de deep learning. Elle permet de créer des modèles de manière rapide et concise en utilisant des abstractions de haut niveau telles que des couches de réseaux de neurones (par exemple, des couches Dense, Convolutional, etc.).

- **tf.keras** fait partie de **TensorFlow**, et est maintenant la version officielle de Keras dans TensorFlow. Elle a été intégrée dans TensorFlow à partir de la version 2.0. Cela signifie que lorsque vous installez TensorFlow 2.0 ou une version ultérieure, **tf.keras** fait partie de l'installation par défaut, et il est recommandé d'utiliser **tf.keras** au lieu de la version autonome de **Keras**.

### 3. **DeepFace**

**DeepFace** est une bibliothèque Python de reconnaissance faciale de haut niveau qui s'appuie sur des modèles de deep learning pour effectuer des tâches comme la vérification de l'identité ou la recherche de visages similaires. DeepFace encapsule plusieurs modèles populaires pour la reconnaissance faciale, comme **VGG-Face**, **Google FaceNet**, **OpenFace**, **DeepID**, et **Dlib**.

Lorsqu'il s'agit de l'intégration de **TensorFlow** et **Keras** dans **DeepFace** :

- **TensorFlow** est utilisé comme moteur sous-jacent pour l'entraînement des modèles et l'exécution des calculs.
- **tf.keras** est souvent utilisé dans **DeepFace** pour la construction et l'entraînement des modèles, car il simplifie l'usage de TensorFlow et permet d'utiliser des couches de réseaux de neurones d'une manière plus lisible et facile à maintenir.
- **DeepFace** prend les modèles de reconnaissance faciale (par exemple, **VGG-Face** ou **FaceNet**) qui sont souvent pré-entraînés et les utilise directement pour effectuer des comparaisons entre des visages, en passant par des modèles de réseaux de neurones profonds.

### Explication du flux de travail avec DeepFace

Voici comment les bibliothèques interagissent dans le flux de travail typique de **DeepFace** pour la reconnaissance faciale :

1. **Prétraitement des images** : L'image est d'abord lue et transformée en un format approprié pour être traité par un réseau de neurones. Ce processus peut inclure la redimension de l'image, l'alignement des visages, etc.

2. **Modèle pré-entraîné** : DeepFace charge un modèle de deep learning pré-entraîné, par exemple, **VGG-Face** ou **FaceNet**, qui sont construits à l'aide de **tf.keras** (ou une autre version de Keras intégrée dans TensorFlow). Ces modèles ont été formés sur de grandes bases de données de visages, ce qui leur permet de reconnaître les caractéristiques faciales de manière robuste.

3. **Exécution avec TensorFlow** : Les images sont envoyées à ces modèles via **TensorFlow** (ou **tf.keras**), qui les traite et produit un vecteur d'embeddings (une représentation numérique des caractéristiques du visage).

4. **Comparaison des visages** : DeepFace compare ensuite ces embeddings pour effectuer des tâches comme la vérification du visage ou la recherche d'un visage similaire.

### Résumé de l'interdépendance entre TensorFlow, tf-keras, et DeepFace

- **TensorFlow** : Il sert de moteur de calcul sous-jacent. TensorFlow est responsable de la gestion de la mémoire GPU, de l'exécution des graphes de calculs et de l'entraînement des modèles.
- **tf.keras** : Il est utilisé comme l'API de haut niveau pour définir, entraîner et évaluer les modèles de deep learning. Il offre des outils plus conviviaux pour travailler avec des réseaux de neurones dans **TensorFlow**.
- **DeepFace** : C'est une bibliothèque d'interface de haut niveau qui utilise des modèles de reconnaissance faciale, souvent construits avec **Keras (via tf.keras)** et **TensorFlow**, pour effectuer des tâches de reconnaissance et de comparaison de visages.

### Conclusion

- **TensorFlow** est le moteur de calcul pour les modèles de deep learning.
- **tf.keras** est l'API de haut niveau qui permet de définir et entraîner des modèles dans TensorFlow.
- **DeepFace** utilise ces deux bibliothèques pour simplifier l'accès aux modèles de reconnaissance faciale et offrir des fonctionnalités de comparaison de visages.

C'est cette combinaison de **TensorFlow**, **tf.keras** et **DeepFace** qui permet d'exécuter des modèles de reconnaissance faciale de manière performante.

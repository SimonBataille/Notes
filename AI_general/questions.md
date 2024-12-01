# Questions IA

```
difference jpg, png ?
difference deep learning ? llm ? nlp ?
encodeur vs decodeur ?
c'est le modele ?
Quel lien entre le modele et la librairie ? Lien modele parametres, tokens ?
c'est quoi les parametres du modele ?
resume stable diffusion ? 4 fichiers telecharges, vecteurs, parametres, 
des modeles entraines sur des phrases en anglais ou sur des phrases en francais ?
quels sont les types de tenseurs ? scalaires, vecteurs, matrices, pyTorch, TensorFlow
```

- pyTorch, TensorFlow sont utilises dans l'industrie pour generer des modeles d'IA

- Les IAs prennent en entree des textes, images ou videos mais les reseaux de neurones composant les IAs ne sont pas capables de manipuler les images.jpg, les textes ou les videos directement. Les reseaux de neurones utilisent des tenseurs pour effectuer les calculs. En reconnaissance d'image les tenseurs representent les pixels de l'image => transforment les donnees en info utiles manipulables par l'ordinateur.
Em gros le tenseur c'est les valeurs des pixels dans une matrice sans les metadata de l'image

- TensorFlow permet de realiser le reseau de neurones, keras permet de l'entrainer : `conda install conda-forge::tensorflow`, `conda install conda-forge::keras`

- Keras permet de construire et d'entrainer des modeles de neuronnes

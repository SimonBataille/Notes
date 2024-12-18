from deepface import DeepFace

img_1 = 'tc-1.jpeg'
img_2 = 'tc-3.jpeg'
img_3 = 'tc-3.jpeg'

models = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace"
]

# deepface will download models on the first run
# 24-12-18 16:13:38 - vgg_face_weights.h5 will be downloaded...
# Downloading...
# From: https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5
# To: /home/simon/.deepface/weights/vgg_face_weights.h5
# 100%|██████████████████████████████████████████████████████████████████████████████████████████████| 580M/580M [01:00<00:00, 9.59MB/s]
# result = DeepFace.verify(img_2, img_3)
# print(result)

# for model in models:
#     result = DeepFace.verify(img1_path=img_3, img2_path=img_2, model_name=model)
#     print(result)


result = DeepFace.analyze(img_1, actions=['age', 'gender', 'emotion', 'race'])
print(result)
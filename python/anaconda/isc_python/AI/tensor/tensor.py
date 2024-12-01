import tensorflow as tf
from keras.preprocessing import image
import matplotlib.pyplot as plt

img_path='num_8-8bit.jpg'

img = image.load_img(img_path, target_size=(28, 28))
img_array=image.img_to_array(img)
img_tensor = tf.convert_to_tensor(img_array)

# display tensor
# shape=(28, 28, 3), dtype=float32
# 28 rows, 28 columns of  list[3]
print(img_tensor)

# plot tensor
# normalize RGB to [0, 1]
plt.imshow(img_tensor / 255.0)
plt.axis('off')
plt.show()

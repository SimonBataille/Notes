from keras.models import Sequential
from keras import layers
import numpy as np

# Define the model
model = Sequential()

model.add(layers.Dense(units=3, input_shape=[1]))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
''' Add layers to improve model
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
...
'''
model.add(layers.Dense(units=1))

# Input and output data
entree = np.array([1, 2, 3, 4, 5], dtype=float)  # Convert to NumPy array
sortie = np.array([2, 4, 6, 8, 10], dtype=float)  # Convert to NumPy array

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(x=entree, y=sortie, epochs=100)

# Interactive prediction
while True:
    x = float(input('Nombre : '))  # Convert input to float
    prediction = model.predict(np.array([x], dtype=float))  # Ensure input is a NumPy array
    print('Prediction : ' + str(prediction[0][0]))

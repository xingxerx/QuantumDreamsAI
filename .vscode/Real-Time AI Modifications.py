import tensorflow as tf
import numpy as np

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(256, activation='sigmoid'),
    tf.keras.layers.Dense(128)
])

# Generate holographic distortion patterns
data = np.random.rand(128,128)
output = model.predict(np.expand_dims(data, axis=0))
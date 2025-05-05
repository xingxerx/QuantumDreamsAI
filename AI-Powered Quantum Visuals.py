import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(256,256)  # Quantum noise pattern
plt.imshow(data, cmap='inferno') # Display as an energy-like hologram
plt.show()
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

points = 500
X = np.linspace(-3, 3, points)
y = np.sin(X) + np.random.uniform(-0.5, 0.5, points)
plt.scatter(X, y)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense 
from tensorflow.keras.optimizers import Adam

def plot_decision_boundary(X, y, model):
    x_span = np.linspace(min(X[:, 0]) - 1, max(X[:, 0]) + 1, 50)
    y_span = np.linspace(min(X[:, 1]) - 1, max(X[:, 1]) + 1, 50)
    xx, yy = np.meshgrid(x_span, y_span)
    xx_, yy_ = xx.ravel(), yy.ravel()
    grid = np.c_[xx_, yy_]
    pred_func = model.predict(grid)
    z = pred_func.reshape(xx.shape)
    plt.contourf(xx, yy, z)

np.random.seed(0)
n_pts = 500

X, y = datasets.make_circles(n_samples = n_pts, random_state = 123, 
                             noise = 0.1, factor = 0.2)


model = Sequential()
model.add(Dense(3, input_shape=(2,), activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))
model.compile(Adam(learning_rate=0.01), 'binary_crossentropy', metrics=['accuracy'])
h = model.fit(x=X, y=y, verbose=1, batch_size=20, epochs=100, shuffle='true')


test_x = 0.1
test_y = 0
point = np.array([[test_x, test_y]])
prediction = model.predict(point)
print(prediction)
plt.plot([test_x], [test_y], marker='o', color='black', markersize=10)
plot_decision_boundary(X, y, model)
plt.scatter(X[y==0,0], X[y==0,1], color='orange')
plt.scatter(X[y==1,0], X[y==1,1], color='red')
plt.show()

plt.plot(h.history['accuracy'])
plt.xlabel ('Epoch')
plt.legend(['accuracy'])
plt.title('Accuracy')
plt.show()
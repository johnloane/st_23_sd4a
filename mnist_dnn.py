import numpy as np
import matplotlib.pyplot as plt
import tensorflow.keras
from keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense 
from tensorflow.keras.optimizers import Adam
from keras.utils import to_categorical
from PIL import Image
import random
import requests
import cv2

np.random.seed(0)

def create_model():
    model = Sequential()
    model.add(Dense(10, input_dim=num_pixels, activation='relu'))
    model.add(Dense(30, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(Adam(learning_rate=0.01), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

(X_train, y_train), (X_test, y_test) = mnist.load_data()
assert(X_train.shape[0] == y_train.shape[0]), "The number of images in the training set does not match the number of labels"
assert(X_test.shape[0] == y_test.shape[0]), "The number of images in the test set does not match the number of labels"
assert(X_train.shape[1:] == (28,28)), "The dimensions of the training images are not 28x28"
assert(X_test.shape[1:] == (28,28)), "The dimensions of the test images are not 28x28"

num_of_samples = []
cols = 5
num_classes = 10

fig, axs = plt.subplots(nrows = num_classes, ncols = cols, figsize=(5,10))
fig.tight_layout()
for i in range(cols):
    for j in range(num_classes):
        x_selected = X_train[y_train==j]
        axs[j][i].imshow(x_selected[random.randint(0, len(x_selected - 1)), : :], cmap=plt.get_cmap("gray"))
        axs[j][i].axis("off")
        if i == 2:
            num_of_samples.append(len(x_selected))
plt.show()

plt.figure(figsize=(12, 4))
plt.bar(range(0, num_classes), num_of_samples)
plt.title("Distribution of the training dataset")
plt.xlabel("Class number")
plt.ylabel("Number of images")
plt.show()

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Scale down the variance
X_train = X_train/255
X_test = X_test/255

num_pixels = 784
X_train = X_train.reshape(X_train.shape[0], num_pixels)
X_test = X_test.reshape(X_test.shape[0], num_pixels)
print(X_test.shape)

model = create_model()
print(model.summary())
history = model.fit(X_train, y_train, validation_split=0.1, epochs=15, batch_size = 200, verbose=1, shuffle=1)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['loss', 'validation_loss'])
plt.title('Loss')
plt.xlabel('epoch')
plt.show()

score = model.evaluate(X_test, y_test, verbose=1)
print('Test score: ', score[0])
print('Test accuracy: ', score[1])

url = 'https://colah.github.io/posts/2014-10-Visualizing-MNIST/img/mnist_pca/MNIST-p1815-4.png'
response = requests.get(url, stream=True)
img = Image.open(response.raw)
plt.imshow(img)
plt.show()

img_array = np.asarray(img)
resized = cv2.resize(img_array, (28,28))
gray_scale = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
image = cv2.bitwise_not(gray_scale)
plt.imshow(image, cmap=plt.get_cmap("gray"))
plt.show()

image = image/255
image = image.reshape(1, 784)
prediction = np.argmax(model.predict(image), axis=-1)
print("Predicted digit: ", str(prediction))



         
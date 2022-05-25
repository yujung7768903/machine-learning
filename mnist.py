import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

print(f"shape of x_train: {x_train.shape}")
print(f"shape of y_train: {y_train.shape}")
print(f"shape of x_test: {x_test.shape}")
print(f"shape of y_test: {y_test.shape}")

plt.rcParams['figure.figsize'] = (5,5)
plt.imshow(x_train[0])
plt.show()

x_train = x_train.reshape((60000, 28 * 28)) / 255.0
x_test = x_test.reshape((10000, 28 * 28)) / 255.0

print(f"shape of x_train: {x_train.shape}")
print(f"shape of x_test: {x_test.shape}")
print(x_train)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1200, activation = 'relu', input_shape = (28*28,)),
    tf.keras.layers.Dense(1024, activation = 'relu'),
    tf.keras.layers.Dense(784, activation = 'relu'),
    tf.keras.layers.Dense(512, activation = 'relu'),
    tf.keras.layers.Dense(256, activation = 'relu'),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dense(64, activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'softmax')
])

model.summary()

model.compile(optimizer = 'sgd',
             loss = 'sparse_categorical_crossentropy',
             metrics = ['accuracy'])

model.fit(x_train, y_train,
         epochs = 60,
         verbose = 1,
         validation_split = 0.2)

tets_loss, test_acc = model.evaluate(x_test, y_test)

print(f'테스트 정확도: {test_acc}')
predictions = model.predict(x_test)
print(predictions[0])
print((np.argmax(predictions[0])))
print(y_test[0])
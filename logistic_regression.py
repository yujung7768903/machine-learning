import tensorflow as tf
from tensorflow.keras.models import Sequential

x_data = [[1, 3], [2, 1], [1, 2], [4, 5], [5, 6], [7, 7]]
y_data = [[0], [0], [0], [1], [1], [1]]

tf.model = tf.keras.Sequential()
tf.model.add(tf.keras.layers.Dense(1, input_dim=2, activation='sigmoid'))


sgd = tf.keras.optimizers.SGD(lr=0.1)
tf.model.compile(loss='mse', optimizer=sgd)

tf.model.summary()

tf.model.fit(x_data, y_data, epochs=400)

y_predict = tf.model.predict([[0,1]])
print(y_predict)

y_predict = tf.model.predict([[7,7]])
print(y_predict)
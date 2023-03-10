import tensorflow as tf
import numpy as np

# Definindo os hiperparâmetros
num_inputs = 2
num_hidden = 5
num_outputs = 1
learning_rate = 0.1

# Criando o modelo
inputs = tf.keras.layers.Input(shape=(num_inputs,))
hidden_layer = tf.keras.layers.Dense(num_hidden, activation=tf.nn.relu)(inputs)
output_layer = tf.keras.layers.Dense(num_outputs)(hidden_layer)

model = tf.keras.models.Model(inputs=inputs, outputs=output_layer)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate), loss='mse')

# Treinando o modelo
inputs_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets_train = np.array([[0], [1], [1], [2]])
model.fit(inputs_train, targets_train, epochs=1000, verbose=0)

# Testando o modelo
while True:
    user_input = input('Qual é a soma? ')
    if user_input.lower() == 'sair':
        break
    inputs_test = np.array([[int(user_input.split('+')[0]), int(user_input.split('+')[1])]])
    prediction = model.predict(inputs_test)
    print('Resposta:', prediction[0][0])

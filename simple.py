from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import numpy as np

def make_model():
    model = Sequential()
    model.add(Dense(5, input_dim=2, kernel_initializer="uniform", activation="sigmoid"))
    model.add(Dense(2, input_dim=5, kernel_initializer="uniform", activation="softmax"))
    model.summary()
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])   # metrics 는 여러개 볼수 있어서 꺽세

    return model


if __name__== "__main__":
    mlp = make_model()

    x = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [[1, 0], [0, 1], [0, 1], [1, 0]]

    mlp.fit(x, y, epochs=100)

    result = mlp.predict(x)
    print(result)

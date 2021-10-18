'''
def And_gate(x1, x2):
    w1 = 0.4
    w2 = 0.2
    bias = -0.5

    w_sum = w1 * x1 + w2 * x2 + bias

    if w_sum <= 0:
        return 0
    else:
        return 1

import cv2


if __name__ =="__main__":
    print("(0, 0):", And_gate(0, 0))
    print("(0, 1):", And_gate(0, 1))
    print("(1, 0):", And_gate(1, 0))
    print("(1, 1):", And_gate(1, 1))

# # keras tensor flow 신경망
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

def make_model():
    model = Sequential()
    model.add(Dense(2, input_dim=2, kernel_initializer='normal', activation="sigmoid"))
    model.summary()
    model.compile(optimizer="adam", loss='binary_crossentropy', metrics=['acciracy'])
    return model

def softmax(x):
    e_x = np.exp(x)
    sum_e_x = np.sum(e_x)
    y = e_x / sum_e_x

    return y

if __name__ == "__main__":
    a = np.array([1.0, 1.0, 2.0])
    sm_a = softmax(a)
    print(sm_a)
'''

# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
#
# import numpy as np
#
# def make_model():
#     model = Sequential()
#     model.add(Dense(5, input_dim=2, kernel_initializer="uniform", activation="sigmoid"))
#     model.add(Dense(2, input_dim=5, kernel_initializer="uniform", activation="softmax"))
#     model.summary()
#     model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])   # metrics 는 여러개 볼수 있어서 꺽세
#
#     return model
#
#
# if __name__== "__main__":
#     mlp = make_model()
#
#     x = [[0, 0], [0, 1], [1, 0], [1, 1]]
#     y = [[1, 0], [0, 1], [0, 1], [1, 0]]
#
#     mlp.fit(x, y, epochs=100)
#
#     result = mlp.predict(x)
#     print(result)

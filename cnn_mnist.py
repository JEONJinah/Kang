import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model

def load_dataset(online=False):
    if online:
        (tr_data, tr_label), (te_data, te_label) = tf.keras.datasets.mnist.load_data()
    else:
        path = "mnist.npz"
        (tr_data, tr_label), (te_data, te_label) = tf.keras.datasets.mnist.load_data(path)

    print(tr_data.shape)
    print(te_data.shape)

    return (tr_data, tr_label), (te_data, te_label)


def make_model():
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(5, 5), strides=(1, 1),
                     activation="relu",
                     input_shape=(28, 28, 1),
                     padding="same"))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(64, (5, 5), activation="relu", padding="same"))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Flatten())
    model.add(Dense(1000, activation="relu"))
    model.add(Dense(10, activation="softmax"))
    model.summary()

    model.compile(loss="categorical_crossentropy", optimizer="adam",
                  metrics=["accuracy"])

    return model

# 하이퍼 파라메터
MY_EPOCH = 5
MY_BATCHSIZE = 200
def train(model, x, y):
    model.fit(x, y, epochs=MY_EPOCH, batch_size=MY_BATCHSIZE)
    filename = "cnn_filter32.h5"
    model.save(filename)

if __name__ =="__main__":
    (train_data, train_label), (test_data, test_label) = load_dataset()

    train_data = train_data.reshape(train_data.shape[0], 28, 28, 1)
    train_data = train_data.astype("float32")
    train_data /= 255

    train_label = tf.keras.utils.to_categorical(train_label, 10)

    cnn = make_model()
    # train(cnn, train_data, train_label)

    test_data = test_data.reshape(test_data.shape[0], 28, 28, 1)
    test_data = test_data.astype("float32")
    test_data /= 255
    test_label = tf.keras.utils.to_categorical(test_label, 10)

    filename = "cnn_filter32.h5"
    cnn = load_model(filename)
    cnn.evaluate(test_data, test_label)


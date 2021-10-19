from tensorflow.keras.applications import VGG16
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import numpy as np
import matplotlib.pyplot as plt


def make_model():
    trans_model = VGG16(weights="imagenet",
                        include_top=False,
                        input_shape=(224, 224, 3))
    trans_model.trainable = False

    model = models.Sequential()
    model.add(trans_model)
    # 모델의 출력은 7x7 이 512개 --> 이것을 펴준다.
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation="relu"))
    model.add(layers.Dense(3, activation="softmax"))

    model.summary()

    return model

MY_BATCH_SIZE = 5
def make_data_set(path):
    data_gen = ImageDataGenerator(rescale=1.0/255,
                                  horizontal_flip=True,
                                  width_shift_range=0.1,
                                  height_shift_range=0.1,
                                  fill_mode="nearest")

    data = data_gen.flow_from_directory(directory=path,
                                        target_size=(224, 224),
                                        batch_size=MY_BATCH_SIZE,
                                        class_mode="categorical")

    return data

def show_train_graph(history):
    acc = history.history["accuracy"]
    val_acc = history.history["val_accuracy"]
    loss = history.history["loss"]
    val_loss = history.history["val_loss"]

    x_len = np.arange((len(loss)))
    plt.plot(x_len, acc, marker=".", c="red", label="Train_Acc")
    plt.plot(x_len, val_acc, marker=".", c="lightcoral", label="Val_Acc")

    plt.legend(loc="best")
    plt.grid()
    plt.xlabel("epoch")
    plt.ylabel("acc")
    plt.show()


if __name__ == "__main__":
    my_clf = make_model()
    my_clf.compile(loss="categorical_crossentropy",
                   optimizer="adam",
                   metrics=["accuracy"])

    base_dir ="./orion/"
    train_dir = base_dir + "TrainingSet/"
    val_dir = base_dir + "TestSet/"

    train_set = make_data_set(train_dir)
    val_set = make_data_set(val_dir)

    history = my_clf.fit_generator(train_set,
                                   steps_per_epoch=10,
                                   epochs=10,
                                   validation_data=val_set,
                                   validation_steps=2)

    my_clf.save("orion.h5")
    show_train_graph(history)

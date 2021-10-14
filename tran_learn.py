from tensorflow.keras.applications import VGG16
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np

MY_BATCH_SIZE = 5


def show_train_graph(history):
    acc = history.history["accuracy"]
    val_acc = history.history["val_accuracy"]
    loss = history.history["loss"]
    val_loss = history.history["val_loss"]

    x_len = np.arange((len(loss)))
    plt.plot(x_len, acc, marker=".", c="red", label="Train_Acc")
    plt.legend(loc="best")
    plt.xlabel("epoch")
    plt.ylabel("acc/loss")

    plt.show()



def make_data_set(path):    # 모두의 딥러닝 20p
    data_gen = ImageDataGenerator(rescale=1.0/255)
    data = data_gen.flow_from_directory( # data path 를 주면 알아서 데이터 셋을 만들어라
        directory=path,
        target_size=(224, 224),
        batch_size=MY_BATCH_SIZE,
        class_mode="categorical"
    )

    return data


def make_model():
    # 모델 불러오기
    trans_model = VGG16(weights="imagenet", include_top=False, input_shape=(224, 224, 3))
    # include_top => 최종 분류기를 연결할 것인가 말것인가 결정
    # input_shape => 150,150(크기), 3(채널 수)
    trans_model.trainable = False

    my_model = models.Sequential()
    my_model.add(trans_model)  # 앞에 네트워크를 가져온다.

    my_model.add(layers.Flatten())
    my_model.add(layers.Dense(256, activation="relu"))
    # Dense layer 를 256개로 쌓아주고 activation 함수로 relu 를 사용한다.
    my_model.add(layers.Dense(2, activation="softmax"))
    # output = 2, 출력 값을 2개로 보내주기 위해서 activation 함수로  softmax 를 사용한다.

    my_model.summary()
    # maxpool : 그 영역에서 가장 큰 값만 가져오는 것

    return my_model


if __name__ == '__main__':
    my_clf = make_model()
    my_clf.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    base_dir = "./coopers/"
    train_dir = base_dir + "TrainSet/"
    val_dir = base_dir + "TestSet/"

    train_set = make_data_set(train_dir)
    val_set = make_data_set(val_dir)

    history = my_clf.fit_generator(
        train_set,
        steps_per_epoch=10,
        epochs=10,
        validation_data=val_set,
        validation_steps=2
    )

    my_clf.save("kupffers.h5")

    show_train_graph(history)
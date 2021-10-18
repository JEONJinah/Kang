from tensorflow.keras.models import Sequential          #딥러닝 구동하는 데 필요한 케라스 함수 호출
from tensorflow.keras.layers import Dense
import tensorflow as tf



def load_data():
    path = "mnist.npz"
    (tr_data, tr_label), (te_data, te_label) = tf.keras.datasets.mnist.load_data(path)

    print(tr_data.shape)
    print(te_data.shape)

    return (tr_data, tr_label), (te_data, te_label)
# 하이퍼 파라메타
NUM_L1_NODE = 1400
MY_EPOCH = 10
MY_BATCH = 200

def make_model():           #딥러닝 구조를 결정(모델을 설정하고 실행)
    model = Sequential()

    model.add(Dense(NUM_L1_NODE, input_dim=784, kernel_initializer="normal", activation="relu")) #입력 2, 출력 sigmoid

    model.add(Dense(10, input_dim=NUM_L1_NODE, kernel_initializer="normal", activation="softmax"))

    model.summary()

    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])  #딥러닝 실행

    return model


def train(model, x, y):
    history = model.fit(x, y, epochs=MY_EPOCH, batch_size=MY_BATCH) #학습된당 // batch_size만큼 잘라서 집어넣기//너무 크면 안됑

    model.save("mlp_hd{0}_e{1}.h5".format(NUM_L1_NODE, MY_EPOCH))  #저장

    return history


if __name__ == "__main__":
    (train_data, train_label), (test_data, test_label) = load_data()

    #데이터 모양 변환
    #데이터는 0~1사이의 float으로
    train_data = train_data.reshape(60000, 784)
    train_data = train_data.astype("float32") #int/int 하면 0되니까 float으로 바꿔주기


    train_data /= 255

    test_data = test_data.reshape(10000, 784).astype("float32") / 255

    print(type(train_label[0]))
    print(train_data[0])    # 맨 앞의 데이터 타입이 무엇인지? // unit8 =

    #lable은 one-hot-encoding
    train_label = tf.keras.utils.to_categorical(train_label, 10)
    test_label = tf.keras.utils.to_categorical(test_label, 10)

    #모델 make
    mlp = make_model()

    #  학습
    '''
    #  train_rst = train(mlp, train_data, train_label)
    for i in range (1, 8):
        del mlp
        mlp = make_model()
        MY_EPOCH = i * 5
        history = train(mlp, train_data, train_label)
        print(type(history))
'''
for i in range(1, 8):
        del mlp
        MY_EPOCH = i * 5
        filename = "mlp_hd{0}_e{1}.h5".format(NUM_L1_NODE, MY_EPOCH)
        mlp = tf.keras.models.load_model(filename)
        print("train: ", mlp.evaluate(train_data, train_label, verbose=0)[1])
        print("test: ", mlp.evaluate(test_data, test_label, verbose=0)[1])


    # del mlp
    # mlp = tf.keras.models.load_model("mlp_hd512_e10.h5")
    #
    # test0 = mlp.predict(test_data[0:1])
    # print(test0)
    # print(test_label[0])
    #
    # acc = mlp.evaluate(test_data, test_label, batch_size=MY_BATCH)
    #
    # print(acc)

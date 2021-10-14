import tensorflow

def load_dataset(online=False):  #함수 이름 뒤에 인자를 online로 받겠다.
    if online:
        (tr_data, tr_lable), (te_data, te_lable) = tf.keras.datasets.mnist.load_data()

    else:
        path = "C:/myproject3/인공지능/Kang/mnist.npz"
        (tr_data, tr_lable), (te_data, te_lable) = tf.keras.datasets.mnist.load_data(path)

    return (tr_data, tr_lable), (te_data, te_lable)

(train_data, train_lable), (test_data, test_lable) = load_dataset()

print(train_data[0].shape)
print(train_data.shape)
print(train_lable.shape)
print(train_lable[0:10])

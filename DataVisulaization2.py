# #  Salmon-Bass (학습데이터처리)
#
import pandas as pd
import matplotlib.pyplot as plt
#
# df = pd.read_csv("salmon_bass_data.csv")   # 정보 불러오기
#
# salmon = df.loc[df["Class"] == "Salmon"]
# bass = df.loc[df["Class"] == "Bass"]
# # print(salmon)
# # print(bass)
#
# plt.title("Length Hisogram")
# plt.hist(salmon["Length"], bins=20, alpha=0.5, label="Salmon")
# plt.hist(bass["Length"], bins=20, alpha=0.5, label="Bass")
# plt.legend(loc="best")
# plt.show()
#
# plt.title("Lightness Hisogram")
# plt.hist(salmon["Lightness"], bins=20, alpha=0.5, label="Salmon")
# plt.hist(bass["Lightness"], bins=20, alpha=0.5, label="Bass")
# plt.legend(loc="best")
# plt.show()
#
# plt.title("Scatter")
# plt.xlabel("Length")
# plt.ylabel("Lightness")
#
# plt.scatter(salmon["Length"], salmon["Lightness"], color="blue", label="Salmon")
# plt.scatter(bass["Length"], bass["Lightness"], color="red", label="Bass")
#
# plt.legend(loc="best")
# plt.show()


# Decision Tree 간단한 2개의 클래스

from sklearn import tree
import numpy as np

df = pd.read_csv("salmon_bass_data.csv")

X = []
Y = []

for i in range(len(df)):
    x = [df.loc[i, "Length"], df.loc[i, "Lightness"]]
    X.append(x)
    Y.append(df.loc[i, "Class"])


dtree = tree.DecisionTreeClassifier()
dtree = dtree.fit(X, Y)

plt.figure(figsize=(10, 10))
tree.plot_tree(dtree, fontsize=8, filled=True)
plt.show()

result = dtree.predict([[2, 2], [0, 1]])
print(result)


# dtree.predict([[2,2], [0,1]])
# print(result)



# for i in range(len(X)):
#     if Y[i] == 0:   #0번 class이면
#         plt.scatter(X[i][0], X[i][1], color="red")
#
#     elif Y[i] == 1:
#         plt.scatter(X[i][0], X[i][1], color="blue")
#
# plt.xlabel("X[0] Feature")
# plt.xticks(np.arange(-1, 3, 1))
# plt.ylabel("X[1] Feature")
# plt.yticks(np.arange(-1, 3, 1))
# plt.grid()
# plt.show()
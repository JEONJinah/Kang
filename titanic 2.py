import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv("titanic/train.csv")
df_test = pd.read_csv("titanic/test.csv")

df_train["Survived"] = df_train["Survived"].replace(0, "Dead").replace(1,"Alive")

df_train["Pclass"] = df_train["Pclass"].replace(1, "1st").replace(2,"Business").replace(3,"Economy")

# 생존 그룹 / 비생존 그룹으로 분리
df_surv = df_train.loc[df_train["Survived"] == "Alive"]
df_dead = df_train.loc[df_train["Survived"] == "Dead"]

df_surv["SibSp"].value_counts().plot(
   kind="bar", label="Alive", color="blue",alpha=0.5
 )
# Sibsp 별로 나누기
df_dead["SibSp"].value_counts().plot(
     kind="bar", label="Dead", color="red",alpha=0.5
 )
plt.legend(loc="best")
plt.show()

# Parch별로 나누기
df_surv["Parch"].value_counts().plot(
   kind="bar", label="Alive", color="blue",alpha=0.5
 )
df_dead["Parch"].value_counts().plot(
     kind="bar", label="Dead", color="red",alpha=0.5
 )
plt.legend(loc="best")
plt.show()

#  Embarked별로 나누기
df_surv["Embarked"].value_counts().plot(
   kind="bar", label="Alive", color="blue",alpha=0.5
 )
df_dead["Embarked"].value_counts().plot(
     kind="bar", label="Dead", color="red",alpha=0.5
 )
plt.legend(loc="best")

plt.show()
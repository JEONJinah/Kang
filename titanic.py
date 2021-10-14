import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

df_train = pd.read_csv("titanic/train.csv")

gt_train = df_train["Survived"]
df_train = df_train.drop(["Name", "PassengerId", "Ticket", "Fare", "Cabin", "Survived"], axis=1)

df_train["Age"] = df_train["Age"].fillna(df_train["Age"].mean())
df_train["Embarked"] = df_train["Embarked"].fillna("S")

df_train["Sex"] = df_train["Sex"].map({"male": 0, "female": 1})

df_train["Embarked"] = df_train["Embarked"].map({"Q": 0, "C": 1, "S": 2})


'''
print(df_train.isnull().sum())
'''
# csf = DecisionTreeClassifier()
csf = RandomForestClassifier()
# csf = SVC()
csf.fit(df_train, gt_train)

print(csf.score(df_train, gt_train))

df_test = pd.read_csv("titanic/test.csv")


pId = df_test["PassengerId"]

df_test = df_test.drop(["Name", "PassengerId", "Ticket", "Fare", "Cabin"], axis=1)

df_test["Age"] = df_test["Age"].fillna(df_test["Age"].mean())
df_test["Embarked"] = df_test["Embarked"].fillna("S")

df_test["Sex"] = df_test["Sex"].map({"male": 0, "female": 1})

df_test["Embarked"] = df_test["Embarked"].map({"Q": 0, "C": 1, "S": 2})

test_result = csf.predict(df_test)

print(test_result)

submit = pd.DataFrame({"PassengerId": pId, "Survived": test_result})

# submit.to_csv("titanic/submit.csv", index=False)

test_gt = pd.read_csv("titanic/groundtruth.csv")

hit = 0
miss = 0

for i in range(len(test_result)):
    if test_result[i] == test_gt["Survived"][i]:
        hit += 1
    else:
        miss += 1


print(hit, miss, round(hit/(hit+miss), 2))
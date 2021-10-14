import pandas as pd
import random as r
import matplotlib.pyplot as plt
#
# def score():
#     return r.randint(0, 100)
#
# aiEng = {'Name': '강현우'}
# print(aiEng)
#
# print(aiEng['Name'])
#
#
# aiEng['Name'] = '전진아'
# print(aiEng)
#
# aiEng['Name'] = ['차혜인', '전진아', '이연우', '김미경']
# print(aiEng)
#
# aiEng['Id'] = [0, 1]
# print(aiEng)
#
# aiEng['Id'].append(2)
# aiEng['Id'].append(3)
# print(aiEng)
#
df = pd.read_csv('ai_score.csv')
# print(df)
#
# print(df.index)
# df['국어'] = 0
# print(df)
#
# df['국어'] = [score(), score(), score(), score()]
# print(df)
#
# df.loc[0] = ['김대현', '2021-1', score()]
# df.loc[1] = ['김동규', '2021-2', score()]
# print(df)
#
# df.loc[df.shape[0]] = ['김미경', '2021-3', score()]
# df.loc[len(df)] = ['김창우', '2021-7', score()]
# df.loc[3] = 0
#
# df.loc[2, 'Id'] = '2021-3'
#
# df.loc[5, 'Id'] = '2021-5'
# df.loc[3] = ['김장원', '2021-4', score()]
# df.loc[2] = ['김미경', '2021-3', score()]
# df.loc[4] = ['김재웅', '2021-5', score()]
# df.loc[5] = ['김지원', '2021-6', score()]
#
# for i in range(len(df), 23):
#     df.loc[i] = ['name-{0}'.format(i), '2021-{0}'.format(i+2), score()]
#
# df.loc[6,'Name'] = '김창우'
# df.loc[7,'Name'] = '박동주'
# df.loc[8,'Name'] = '박종균'
# df.loc[9,'Name'] = '서지완'
# df.loc[10,'Name'] = '손이나'
# df.loc[11,'Name'] = '신나리'
# df.loc[12,'Name'] = '안정현'
# df.loc[13,'Name'] = '이병훈'
# df.loc[14,'Name'] = '이승휘'
# df.loc[15,'Name'] = '이연우'
# df.loc[16,'Name'] = '전진아'
# df.loc[17,'Name'] = '조경민'
# df.loc[18,'Name'] = '차혜인'
# df.loc[19,'Name'] = '추승오'
# df.loc[20,'Name'] = '한창협'
# df.loc[21,'Name'] = '허윤석'
#
# df['수학'] = 0
# df['영어'] = 0
# for i in range(len(df)):
#     df.loc[i, '수학'] = score()
#     df.loc[i, '영어'] = score()
#
# print(df)

import pandas as pd
import matplotlib.pyplot as plt



# plt.hist(df['수학'], bins=20)

canvas = plt.figure(figsize=(7.0, 7.0)) # 이미지 크기 조절
plt.grid() # 격자 표현
# color, marker 모양
plt.scatter(df['수학'], df['영어'],color='red', marker='P')
# 점 하나 씩도 가능
plt.scatter(df.loc[0, '수학'], df.loc[0, '영어'],color='red', marker='P') # 플러스 모양
plt.scatter(df.loc[1, '수학'], df.loc[1, '영어'],color='blue', marker='D') # 다이아몬드
plt.scatter(df.loc[2, '수학'], df.loc[2, '영어'],color='yellow', marker='h') # 헥사곤
plt.scatter(df.loc[3, '수학'], df.loc[3, '영어'],color='green', marker='x') # x
plt.show()

canvas = plt.figure(figsize=(7.0, 7.0))
plt.xlabel('수학 점수')
plt.ylabel('영어 점수')
for i in range(len(df['Sex'])):
    if df['Sex'][i] == '남':
        plt.scatter(df['수학'][i], df['영어'][i], color='blue')

    else:
        plt.scatter(df['수학'][i], df['영어'][i], color='red')

plt.show()
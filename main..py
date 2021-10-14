import MachineLearning1 as ml

numMarine = 0
ml.makeMarine()
numMarine += 1

# print("현재 마린 수는 {0}마리 입니다.".format(numMarine))
#
# ml.marineAttak(1)
#
# #call은 Calculator 클래스의 객체(인스턴스)
# call = ml.Calculator()
#
# finalValue = call.add(10)
# print(finalValue)
#
# call.clear()
# print(call.result)

class Marine:
    def __init__(self, posX, posY):
        print("마린이 생성되었습니다.")
        self.hp = 100
        self.armor = 10
        self.att = 5
        self.posX = posX
        self.posY = posY
    def attack(self, target):
        print("마린이 {0}을(를) 공격합니다.".format(target))

    def move(self, x, y):
        print("마린이 ({0}, {1})에서 ({2}, {3})으로 이동합니다.".format(self.posX, self.posY, x, y))

        self.posX = x
        self.posY = y

m1 = Marine(0, 0)
m2 = Marine(0, 0) #위치는 나중에 배럭의 위치로 대체
m1.attack("탱크")
m2.attack("배틀크루저")
m1.move(100, 100)
m1.move(100, 200)
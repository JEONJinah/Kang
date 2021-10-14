def fruitJuice (fruit):
    juice = fruit + " juice"
    return juice

def add (a, b):
    print('{0}, {1}의 합은 {2}입니다.'.format(a, b, a+b))

def hello() :
    return 'hello'


def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def times(a, b):
    return a * b

def divided(a, b):
    if b != 0:
        return a / b

    else:
        print("Not number")
        return 0

c = add(1, 2)
print(c)

c = minus(5, 2)
print(c)

c = times(2, 3)
print(c)

c = divided(2, 0)
print(c)


def makeMarine():
    print("마린을 한 마리 생성했습니다.")


def marineAttak(MarineID):
    print("마린{0}가 공격합니다. 땅땅".format(MarineID))

class Calculator:
    def __init__(self):
        print("Calculator 객체가 초기화 되었습니다.".format())
        self.result = 0
    #result를 0으로 만드는 함수
    def clear(self):
        self.result=0
    def add(self, value):
            self.result += value
            return self.result

    def subtract(self, value):
            self.result -= value
            return self. result

    def times(self, value):
        self.result *= value
        return self.result

    def divided(self, value):
        if value != 0:
            self.result /= value
        else:
            print("Cannot divided by Zero")
        return self.result
Cal1 = Calculator()
Cal1.clear()
print(Cal1.result)
print(Cal1.add(10))
print(Cal1.subtract(2))
print(Cal1.times(2))
print(Cal1.divided(3))





num = int(input())

if num + 20 > 255:
    num = 255

else:
    num = num+20

print(num)

num = int(input())
if num - 20 < 0:
    num = 0
elif num + 20 > 255:
    num = 255
else:
    num = num+20
print(num)

'''
year = int(input("년도를 입력하세요."))

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print("{0}은 윤년입니다.".format(year))
else:
    print("{0}은 윤년이 아닙니다.".format(year))


fruit = ["사과", "귤", "수박"]
for 변수 in fruit:
    print("#####")

fruit = ["사과", "귤", "수박"]
for 변수 in fruit:
    print(변수)


변수 = {10, 20, 30}
for 변수 in 변수:
    print(변수)

for X in [10, 20, 30]:
    print()


변수 = {"10", "20", "30"}
for x in 변수:
    print(변수)
    print("-----")


for x in [3, -20, -3, 44]:
  if x<0:
    print(x)


for x in [3, 100, 23, 44]:
    if x %3 == 0:
        print(x)

count = 1
while count <= 10:
   print ("hello world - {0}".format(count))
   count = count + 1
   if count > 10:
   break


count = 10
while count <= 10:
    print ("hello world - {0}".format(count))
    count = count - 1
    if count <= 0:
        break


count = 10
while count > 0:
    print('hello wolrd - {0}'.format(count))
    count = count -1

count = 1
while count <= 10:
    if count % 2 == 1:
        print(count)
    else:
        break
    count += 1


n = 1
d = 5
An = 5 * n - 3
while An < 200:
    n = n + 1
    An = 5 * n - 3

print("A{0} = {1}".format(n-1, An - d))



quantity = 2
coffeePrice = 300

while quantity > 0:
    money = int(input("돈을 넣으세요: "))

    if money >= coffeePrice:
        print("커피가 나옵니다. 잠시 기다리세요")
        print("거스름돈은 {0}원 입니다.".format(money-coffeePrice))
        quantity -= 1 #quantity = quantity - 1

    if money < coffeePrice:
        print("돈을 더 넣어주세요.".format(coffeePrice))

    else:
        print("{0}원 이상의 금액을 주세요.".format(coffeePrice))
        print("남은 커피 수량은 {0}개 입니다.".format(quantity))

print("남은 커피가 없습니다. 종료합니다.")



quantity = 3
coffeePrice = 300

while quantity > 0:
    money = int(input("돈을 지불하세요."))

    if money >= coffeePrice:
        print("커피가 나옵니다. 잠시만 기다리세요")
        print("거스름돈은 {0}원 입니다.".format(money-coffeePrice))
        quantity -= 1

    if money < coffeePrice:
        print("돈이 부족합니다. {0}원 이상의 금액을 주세요.".format(coffeePrice))

    else:
        print("남은 커피 수량은 {0}개 입니다.".format(quantity))

print("감사합니다. 안녕히가세요.")


quantity = 3
coffeePrice = 300

while quantity > 0:
    money = int(input("돈을 넣으세요."))

    while money < 300:
        addMoney = int(input("돈을 더 넣으세요.".format(money)))
        if addMoney == 0:
            print("현재 금액: {0}을 반환합니다. ".format(money))
        money += addMoney

    else:
        print("잠시만 기다려주세요. 거스름돈은 {0}원 입니다. ".format(money-coffeePrice))
        print("남은 커피 수량은 {0}개 입니다.".format(quantity))

print("감사합니다.")
'''
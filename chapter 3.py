'''


# [3-2]
age = int(input('나이 입력 : '))
fee = 2000
if(age >= 65):
    fee = 0
print('나이: ', age)
print('요금: ', fee)


# [3-3]
a = int(input('정수입력 : '))
if(a%2 == 1):
    print('홀수')
else:
    print('짝수')


# [3-4]
excel, powpoint, word = input("정수를 입력하시오: ").split()

excel = int(excel)
powpoint = int(powpoint)
word = int(word)

sum = excel + powpoint + word
avr = sum / 3

print('합계:{0}'.format(sum))
print('평균:{0}'.format(round(avr, 2)))
if avr >= 60:
    print('합격')
else:
    print('불합격')

# [3-5]

excel, powpoint, word = input("정수를 입력하시오: ").split()

excel = int(excel)
powpoint = int(powpoint)
word = int(word)

sum = excel + powpoint + word
avr = sum / 3

print('합계:{0}'.format(sum))
print('평균:{0}'.format(round(avr, 2)))
if excel < 40 or powpoint < 40 or word < 40 or avr < 60:
    print('불합격')
else:
    print('불합격')


# [3-6]

score = int(input('점수를 입력하세요: '))
grade = 'F'

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score  >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'

print('당신의 점수는 {0} 입니다.'.format(grade))


# [3-7]
num1, oper, num2 = input('수식을 입력하세요'
                         'ex) 2 + 3 :').split()
num1 = int(num1)
num2 = int(num2)

if oper == '+':
    print('{0} + {1} = {2}'.format(num1, num2, num1+num2))
elif oper == '-':
    print('{0} - {1} = {2}'.format(num1, num2, num1-num2))
elif oper == '*':
    print('{0} * {1} = {2}'.format(num1, num2, num1 * num2))
elif oper == '/':
    print('{0} / {1} = {2}'.format(num1, num2, num1/num2))

else :
    print('잘못된 연산자 입니다.')

# [3-8]

i = 1
sum = 0
while i <= 10:
    sum = sum + i
    i = i +1
print(sum)


# [3-9]

start, end = input('2개의 숫자 : ').split()
# 숫자(int)로 캐스팅
start = int(start)
end = int(end)
sum = 0

while start <= end:
    sum = sum + start
    start = start + 1

print(sum)

# [3-9]
start, end = input('2개의 정수 입력: ').split()
start = int(start)
end = int(end)
sum = 0


while start <= end:
    if start < end
        print(start, '+', end=' ')
    else:
        print(start, '=', end=' ')

    sum = sum + start
    start = start + 1

print(sum)

# [3-9 +1 ]
start, end = input('2개의 숫자 : ').split()
# 숫자(int)로 캐스팅
start = int(start)
end = int(end)
sum = 0

while start <= end:
    if start < end:
        print(start, '+', end=' ')
    elif start == end:
        print(start, '=', end=' ')
    sum = sum + start
    start = start + 1

print(sum)

# [3-9 +2]
start, end = input('2개의 숫자 : ').split()

start = int(start)
end = int(end)
sum = 0

if start > end:
    temp = start
    start = end
    end = temp

while start <= end:
    if start < end:
        print(start, '+', end=' ')
    elif start == end:
        print(start, '=', end=' ')
    sum = sum + start
    start = start + 1

print(sum)


# [3-10]
sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)


# [3-12]
for i in range (1, 10):
    print('2 * {0} = {1}'. format(i, 2*i))




# [3-12 -1 ]
n = int(input('단수를 입력하세요: '))
i = 1
while i < 10:
    print('{0} * {1} = {2}'.format(n, i, n*i))
    i= i+1

 # [3-12-2]
n= int(input('단수를 입력하세요: '))
i = 1
while i < 10:
    print('{0} * {1} = {2}'.format(n, i, n*i))
    i= i+1


# [3-13]
sum = 0
for i in range  (100):
    if i % 3 == 0:
        sum = sum + i
        print(i, end = '')

print('\n', sum)


# [3-13-2]
sum= 0
for i in range (1, 100):
    An = 3*i-2
    Sn = S*i + An
        Si = Si + i
        print(i, end = '100')
print('\n', sum)



'''




# # [3-1]
# age = input("나이: ")
# fee = 2000
# if(int(age) >= 65):
#     fee = 0
# else :
#     print('요금: 2000')

# [3-15]


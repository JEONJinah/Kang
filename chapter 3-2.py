# age = input("나이: ")
# fee = 2000
# if (int(age) >= 65):
#     fee = 0
# else:
#     print('요금: 2000')

# age = int(input('나이 입력:'))
# fee = 2000
# if(age >= 65):
#     fee = 0
# print('나이:', age)
# print('요금:', fee)

# a = int(input('정수입력:'))
# if(a%2 == 1):
#     print('홀수')
# else:
# #     print('짝수')
#
# excel, powpoint, word = input("정수를 입력하세요: ").split()
#
# excel = int(excel)
# powpoint = int(powpoint)
# word = int(word)
#
# sum = excel + powpoint + word
# avr = sum / 3
#
# print('합계:{0}'.format(sum))
# print('평균:{0}'.format(avr, 2))
# if avr >= 60:
#     print('합격')
# else:
#     print('불합격')

# excel, powpoint, word = input("정수를 입력하세요: ").split()
#
# excel = int(excel)
# powpoint = int(powpoint)
# word = int(word)
#
# sum = excel + powpoint +word
# avr = sum / 3
#
# print('합계: {0}'.format(sum))
# print('평균: {0}'.format(avr))
# if excel < 40 or powpoint < 40 or word < 40 or avr < 60:
#     print('불합격')
# else:
#     print('합격')
#
# score = int(input('학생 점수 입력: '))
# grade = 'E'
#
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# print('당신의 점수는 {0}입니다.'.format(grade))

# i = 1
# sum = 0
# while i <= 10:
#     sum = sum + i
#     i = i + 1
# print(sum)
# #3-9 부연설명
# start, end = input('2개의 정수 입력').split()
# start = int(start)
# end = int(end)
# sum = 0
#
# if start > end:
#     temp = start
#     start = end
#     end = temp
# print(start, end)
#
# while start <= end:
#     if start < end:
#         print(start, "+", end=" ")
#     else:
#         print(start, "=", end=" ")
#
#     sum = sum + start
#     start = start + 1
# print(sum)
#
# sum = 0
# for i in range(1, 20):
#     sum = sum + i
# print(sum)
#
# for i in range (1, 10):
#     print('3 * {0} = {1}'.format(i, 3*i))
#

# n = int(input('단수를 입력하세요: '))
# i = 1
# while i < 10:
#     print('{0} * {1} = {2}'.format(n, i, n*i))
#     i= i+1

# sum = 0
# for i in range (100):
#     if i % 3 == 0:
#         sum = sum + i
#         print(i, end = '')
#
# print('\n', sum)
#
# sum = 0
# for i in range  (100):
#     if i % 3 == 0:
#         sum = sum + i
#         print(i, end = '')
#
# print('\n', sum)
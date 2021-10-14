'''

# [2-7]
input1, input2 =input().split()
print('반환 값: {0}, {1}\n'.format(input1, input2))


# [2-8]
age = input()
print("나이: {0}".format(age))

# [2-9]
height = input()
print("키: {0}".format(height))

# [2-10]
linuxScore, javaScore, cScore = input().split()
print('Linux: {0}'.format(linuxScore))
print('Java: {0}'.format(javaScore))
print('C: {0}'.format(cScore))

# [2-11]
bloodType = input()
print('혈액형: {0}'.format(bloodType))

# [2-12]
affilation = input()
print('소속: {0}'.format(affilation))

# [2-13]
digit1, operation, digit2 = input().split()
print('첫 번째 숫자: {0}'.format(digit1))
print('수식: {0}'.format(operation))
print('두 번째 숫자: {0}'.format(digit2))

# [2-15]
fp = open('input.txt', 'r')
inputData = fp.readline()
print('입력 값: {0}'.format(inputData))
fp.close()

# [2-16]
fp = open('input.txt', 'r')
inputData = fp.readline().split()
print(inputData)
fp.close()

# [2-17]
fp = open('input.csv', 'r')
print('리눅스\t자바\tc언어')

data = fp.readlines()
for rows in data:
    rows = rows.rstrip('\n')
    cols = rows.split(',')
    for col in cols:
        if col !='\n':
            print(col, '\t', end='')
    print()

fp.close()
'''

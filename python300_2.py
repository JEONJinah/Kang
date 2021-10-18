'''
# 151
list = [3, -20, -3, 44]
for i in list:
    if i < 0:
        print(i)

# 152
list = [3, 100, 23, 44]
for i in list:
    if i % 3 == 0:
        print(i)

# 153
list = [13, 21, 12, 14, 30, 18]
for i in list:
    if i % 3 == 0 and i < 20:
        print(i)

# 154
list = ["I", "study", "python", "language", "!"]
for i in list:
    if len(i) >= 3:
        print(i)

# 155
list = ["A", "b", "c", "D"]
for i in list:
    if i.isupper():
        print(i)

# 156
list = ["A", "b", "c", "D"]
for i in list:
    if i.islower():
        print(i)

for i in list:
  if i.isupper() != True:
    print(i)

# 157
list = ['dog', 'cat', 'parrot']
for i in list:
    print(i[0].upper() + i[1:])

# 158
list = ['hello.py', 'ex01.py', 'intro.hwp']
for i in list:
    split = i.split(".")
    print(split[0])   # .split() 괄호를 중심으로 뒤에거를 뺀다.

# 159
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list:
    split = i.split(".")
    if split[1] == "h":
        print(i)

# 160
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list:
    split = i.split(".")
    if (split[1] == "h") or (split[1] == "c"):
        print(i)

# 161
for i in range(100):
    print(i)

# 162
for i in range(2002, 2050,4):
    print(i)

# 163
for i in range(3, 31, 3):
    print(i)

# 164
for i in range(100):
    print(99 - i)

# 165
for i in range(10):
    print(i / 10)

# 166
for i in range(1, 10):
    print(3, "x", i, "=", 3*i )

# 167
num = 3
for i in range(1, 10, 2):
    print(num, "x", i, " = ", num * i)

num = 3
for i in range(1, 10) :
    if i % 2 == 1 :
        print (num, "x", i, " = ", num * i)

# 168
sum = 0
for i in range(1, 11):
    sum += i
print("합 :", sum)

# 169
sum = 0
for i in range(1, 11, 2):
    sum += i
print("합:", sum)

# 170
result = 1
for i in range(1, 11):
    result *= i
print(result)

# 171
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

# 172  # 우예 풀어
price_list = [32100, 32150, 32000, 32500]
for i in range(price_list):
    print(i, price_list)

# 173  # 3-i 왜 하는거?
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(3 - i, price_list[i])

# 174
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i + 100, price_list[i])

# 175
my_list = ["가", "나", "다", "라"]
print(my_list[0], my_list[1])
print(my_list[1], my_list[2])
print(my_list[2], my_list[3])

for i in [0, 1,2]:
    print(my_list[i], my_list[i+1])
'''
# 176
my_list = ["가", "나", "다", "라", "마"]
print(my_list[0], my_list[1], my_list[2])
print(my_list[1], my_list[2], my_list[3])
print(my_list[2], my_list[3], my_list[4])

for i in [0, 1, 2, 3]:
    print(my_list[i], my_list[i+1], my_list[i+2])

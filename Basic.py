

str1 = "%-10sjane" % ("hi")
print(str1, len(str1))

print(f"{3.42134234:0.4f}")
str2 = f"{3.42134234:0.4f}"
print(str2, len(str2))
#
# str1 = """
# My name is JeonJinah.
# I love WOODowhan.
# He is really handsome.
# """
#
# cnt_is = str1.count("is")
# print(cnt_is)
# # print(str1.find("name"), str1.index("n"))
# # print(str1.upper())
# #
# str1 = "12345"
# print(",".join(str1))
#
# str_list = "Life is too short"
# print(str_list.replace("short", "long"))
# print(str_list)
#
# str_list = str1.split()
# print(str_list, type(str_list))


# # list 사용법
# list1 = [1, 2, 3, 1.7]
# print(f'{list1}, {list1[0]}, {list1[1]}, {list1[2]}')
# list2 = [30, 3, ["study", "bed", "game"], "10층", "3억5천"]
# print(list2)
#
# list3 = []
# list3.append("1")
# list3.append(4.6)
# print(list3, type(list3[0]), type(list3[1]))
#
# #list indexing example
# print(list2[-3][0])
# str2 = f'My house area is {list2[0]}, there are {len(list2[-3])} rooms\n I like the {list2[-3][2]} room'
# print(str2)

# languages = ['python', 'perl', 'c', 'java']
#
# for lang in languages:
#     if lang in ['python', 'perl']:
#         print("%6s need interpreter" % lang)
#     elif lang in ['c', 'java']:
#         print("%6s need compiler % lang")
#     else:
#         print("should not reach here")
#
# import time
# #0(1)
# a1, b1, c1 = 5, 6, 2.7
# sum_num = a1 + b1 + c1
# print(sum_num)
#
# # 0(N)
# arr = list(range(1, 100000))
# sum_num = 0
# for idx in arr:
#     sum_num += idx
# print(f'sum of 1 to 100000 equal is {sum_num}')
#
# # 0(N^2)
# start_time = time.time()
# arr = list(range(1, 10000))
# for i in arr:
#     for j in arr:
#         tmp = i * j
# end_time = time.time()
# print(f"수행시간은 {end_time-start_time} 입니다.")

import time
from random import randint

# list 생성, random 값을 list에 append
arr = []
# for _ in range(100000):
#     arr.append(randint(1, 10000))

for _ in range(100000):
    arr.append(randint(1, 100000))
# Selected Sort Algorithm
start_time = time.time()
print(len(arr))
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] =arr[min_idx], arr[i]

print(arr[0:50])
end_time = time.time()
print(f'선택 정렬의 수행시간은 {len(arr)} 때, 선택영역의 수행시간은 {end_time-start_time}입니다.')




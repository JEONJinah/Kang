# # 변수 할당
# a = 1
# b = "python"
# c = [1, 2, 3]
# print(a, b, c)
#
# a = [1, 2, 3]
# b = a
# a[2] = ['1', '2']
# print(f'a={a}, b={b}')
# print(id(a), id(b))

# a = [1, 2, 3]
# b = a[:]
# c = a.copy()
# print(id(a), id(b), id(c))
#
# a, b = 1, 2
# a, b = (1, 2)

# # 이진 탐색 연습
# # 데이터의 갯수를 입력받고, 데이터는 랜덤한 값으로 채우자.
#
# # 만약에 랜덤한 값을 사용했을 경우
# # pL, pR, pC = 인덱스 값
# # list_arr.sort()
#
# list_arr = list(range(10000001))
# find_num = 10000000
#
# pL, pR = 0, len(list_arr)-1
# cnt_num = 0  # print(f'{cnt_num} 번만에 값을 찾았음') 을 쓰기 위해
# while 1:
#     pC = (pL + pR) // 2  # 리스트의 중간 index 값을 구하기 위해
#     cnt_num += 1
#     if list_arr[pC] == find_num:
#         print(f'{cnt_num} 번만에 값을 찾았음')
#         break
# # 매번 변경되는 중앙 index 값보다 찾는 값이 크면 -->
# # 매번 변경되는 중앙 index 값보다 찾는 값이 크면 <--
#     elif list_arr[pC] < find_num:
#         pL = pC + 1
#     else:
#         pR = pC - 1
#     if pL > pR:
#         print("찾는 값이 없음")
#         break

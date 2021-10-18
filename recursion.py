# def factorial(n: int) -> int:
#
#     if n > 0:
#         return n * factorial(n-1)
#     else:
#         return 1
#
# if __name__ == '__main__':
#     n = int(input('출력할 팩토리얼값을 입력하세요: '))
#     print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')

# def factorial_for(n):
#     result = 1  #result *= 1 <==result는 1이 되어야 함
#     for i in range(1, n+1):  #range = <1 ~ n-1>
#         result *= i
#     return result
#
# def factorial(n):
#     if n > 0:
#         return n * factorial(n-1)
#     else:
#         return 1
#
# # dynamic program에서 bottom up 방식으로 구현한 것
# def fibo_for(n):
#     dp_table = [0] * (n+1)  #[0] * n <=== 인덱스가 1부터 값을 넣음
#     if n == 1 or n == 2:
#         return 1
#     else:
#         dp_table[1] = 1
#         dp_table[2] = 1
#         for i in range(2, n+1):
#             dp_table[i] = dp_table[i-2] + dp_table[i-1]
#     return dp_table[n]
#
# # 재귀함수로 피보나치 수열 구현
# # 코드는 간결 but 계산 복잡도 측면에서 사용 불가능
# # 복잡도 O(2^n)   n>40 이상이면, 엄청 시간 많이 걸림
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibo(n-2) + fibo(n-1)
#
# # memorization -- dynamic program에서 top-down 방식
# dp = [0] * 100
# def fibo_mem(n):
#     if n ==1 or n ==2:
#         return 1
#     if dp[n] != 0:
#         return dp[n]
#     dp[n] = fibo_mem(n-2) + fibo_mem(n-1)
#
# print(fibo(40))

# # 이진 검색 알고리즘의 실행 과정을 출력
# from typing import Any, Sequence
#
# def bin_search(a: Sequence, key: Any) -> int:
#
#     pl = 0
#     pr = len(a) - 1
#
#     print('    |', end='')
#     for i in range(len(a)):
#         print(f'{i : 4}', end='')
#     print()
#     print('---+' + (4 * len(a) + 2) * '-')
#
#     while True:
#         pc = (pl + pr) // 2
#
#         print('  |', end='')
#         if pl != pc:
#             print((pl * 4 + 1) * ' ' + '<-' + ((pc - pl) * 4) * ' ' + '+', end='')
#         else:
#             print((pc * 4 + 1) * ' ' + '<+', end='')
#         if pc != pr:
#             print(((pr-pc) * 4 - 2) * ' ' + '->')
#         else:
#             print('->')
#         print(f'{pc:3}|', end='')
#         for i in range(len(a)):
#             print(f'{a[i]:4}', end='')
#         print('\n   |')
#         if a[pc] == key:
#             return pc
#         elif a[pc] < key:
#             pl = pc + 1
#         else:
#             pr = pc - 1
#         if pl > pr:
#             break
#         return - 1
#
# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요.: '))
#     x = [None] * num
#
#     print('배열 데이터를 오름차순으로 입력하세요.')
#
#     x[0] = int(input('x[0]: '))
#
#     for i in range(1, num):
#         while True:
#             x[i] = int(input(f'x[{i}]: '))
#             if x[i] >= x[i - 1]:
#                 break
#
#     ky = int(input('검색할 값을 입력하세요.: '))
#
#     idx = bin_search(x, ky)
#
#     if idx == -1:
#         print('검색값을 갖는 원소가 존재하지 않습니다.')
#
#     else:
#         print(f'검색값은 x[{idx}]에 있습니다.')

# # 이진 탐색 소스코드 구현 (재귀 함수)
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     # 찾은 경우 중간점 인덱스 반환
#     if array[mid] == target:
#         return mid
#     # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
#     else:
#         return binary_search(array, target, mid + 1, end)
#
# # n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
# n, target = list(map(int, input().split()))
# # 전체 원소 입력 받기
# array = list(map(int, input().split()))
#
# # 이진 탐색 수행 결과 출력
# result = binary_search(array, target, 0, n - 1)
# if result == None:
#     print("원소가 존재하지 않습니다")
# else:
#     print(result + 1)

# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

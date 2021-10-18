n = int(input())  #찾고자 하는 데이터
array = list(map(int, input().split()))   #공백을 기준으로 가져오겠다.
m = int(input())   #데이터 갯수
find_x = list(map(int, input().split()))

result_bin = []
array.sort()
print(f'N개의 Dataset은 {array}입니다.')

for idx in find_x:
    pL, pR = 0, len(array) - 1
    while 1:
       pC = (pL + pR) // 2
       if array[pC] == idx:
           result_bin.append(array[pC])
           break
        elif idx > array[pC]:
            pL = pC + 1
        else:
            pR = pC - 1
        if pL > pR:
            break
print(f'N list에서 찾은 값은 {result_bin}')

# def f(x):
#     y = x + 3  # y 는 지역변수
#     return y
#
# y = f(3)   # 위에 y랑 밑에 y가 다르다.
# print(y)


# min_max 구하기
def min_max(int_list):
    min_val = int_list[0]
    max_val = int_list[0]

    for idx in range(1, len(int_list)):
        if min_val > int_list[idx]:
            min_val = int_list[idx]

        if max_val < int_list[idx]:
            max_val = int_list[idx]

    return min_val, max_val  # min_val는 지역변수

#
def trim_mean(int_list):
    min_val, max_val = min_max(int_list)
    print(max_val)
    int_list.remove(min_val)
    int_list.remove(max_val)

    sum = 0

    for elem in int_list:
        sum += elem

    avr = sum / len(int_list)
    return avr

list_a = [1, 2, 3, 4, 5]
print(trim_mean(list_a))

def even_list(int_list):
    e_list = []

    for elem in int_list:
        if elem % 2 == 0:
            e_list.append(elem)

    return e_list
list_a = [1, 2, 3, 4, 5, 6]
print(even_list(list_a))
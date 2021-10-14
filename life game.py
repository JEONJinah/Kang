def calNext(cur):
    retVal = list(cur)

    for i in range(len(cur)):
        prev = i - 1
        next = i + 1
        if i + 1 == len(cur):
            next = 0

        if cur[prev] == cur[next]:
            retVal[i] = str(cur[i])
        else:
            if cur[i] == '0':
                retVal[i] = '1'
            else:
                retVal[i] = '0'

    return ''.join(retVal)

target = "0001"
candidate = ["00", "01", "10", "11"]
result = []

while candidate:
    a = candidate.pop()
    a1 = a + '0'
    a2 = a + '1'

    n1 = calNext(a1)
    n2 = calNext(a2)

    if len(n1) != len(target):
        # 처음것과 마지막 것은 비교하지 않음
        if n1[1:-1] == target[1:len(n1) - 1]:
            candidate.append(a1)
        if n2[1:-1] == target[1:len(n2) - 1]:
            candidate.append(a2)

    else:
        if n1 == target:
            result.append(a1)
        if n2 == target:
            result.append(a2)

print(result)
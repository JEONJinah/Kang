userInput = input();

print(userInput)

inputlist = list(userInput)
print(inputlist)

def calNext(cur):
    retVal = list(cur)

    for i in range(len(cur)):
        prev = i - 1
        next = i + 1
        if i + 1 == len(cur):
            
import numpy as np
import sys
from collections import deque

apart = np.array([[0, 1, 1, 0, 1, 0, 0],
                  [0, 1, 1, 0, 1, 0, 1],
                  [1, 1, 1, 0, 1, 0, 1],
                  [0, 0, 0, 0, 1, 1, 1],
                  [0, 1, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 0, 0, 0]])

def bfs(x, y):
    dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    queue = deque([(x, y)])
    size = 0
    while queue:
        item = queue.popleft()
        for xy in dxy:
            new_x = int(item[0] + xy[0])
            new_y = int(item[1] + xy[1])
            if 0 <= new_x < apart and 0 <= new_y < apart and check[new_x][new_y] != 1:
                if maps[new_x][new_y] == maps[item[0]][item[1]]:
                    queue.append((new_x, new_y))
                    check[new_x][new_y] = 1
                    size += 1

    return size


answer = []
maps = []
check = [[0 for _ in range(apart)] for _ in range(apart)]
for _ in range(apart):
    tmp_map = list(sys.stdin.readline())
    tmp_map.remove('\n')
    maps.append(tmp_map)

for i in range(apart):
    for j in range(apart):
        if maps[i][j] != '0':
            if check[i][j] != 1:
                answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for item in answer:
    if item == 0:
        print(1)
    else:
        print(item)

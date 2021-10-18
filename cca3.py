import numpy as np


ice_case = np.array([[0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1],
                    [1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0]])

apeach = np.array([[1, 1, 1, 0],
                   [1, 2, 2, 0],
                   [1, 0, 0, 1],
                   [0, 0, 0, 1],
                   [0, 0, 0, 3],
                   [0, 0, 0, 3]])


apart = np.array([[0, 1, 1, 0, 1, 0, 0],
                  [0, 1, 1, 0, 1, 0, 1],
                  [1, 1, 1, 0, 1, 0, 1],
                  [0, 0, 0, 0, 1, 1, 1],
                  [0, 1, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 0, 0, 0]])

maze = np.array([[1, 0, 1, 0, 1, 0],
                [1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]])


'''
def dfs(cur_x, cur_y, label, src, ans, val):
    stack = [[cur_x, cur_y]]
    rows, cols = src.shape


    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    cnt = 0

    while stack:
        x, y = stack.pop()

        if ans[y, x] == 0:
            ans[y, x] = label
            cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 예외처리
            if nx < 0 or ny < 0 or nx >= cols or ny >= rows:
                continue

            if src[ny, nx] == val and ans[ny, nx] == 0:
                stack.append([nx, ny])

    return cnt

def sol1():
    ans1 = np.zeros(apart.shape, dtype=np.uint8)

    cur_label = 0


    for y in range(apart.shape[0]):
        for x in range(apart.shape[1]):
            # 값이 있고 방문 전이면
            if apart[y, x] == 1 and ans1[y, x] == 0:
                cur_label += 1
                cnt = dfs(x, y, cur_label, apart, ans1, 1)
                print("label {0}은 {1}개입니다.".format(cur_label, cnt))
    print(ans1)

    # BFS로 단지 확인 알고리즘
    def bfs(house, i, j, N, visited):

        if house[i][j] == 0:  # 0일 경우 함수를 넘김
            visited.append([i, j])
            return [0, visited]

        block = []  # 함수 안에서만 쓰일 블록
        queue = [[i, j]]  # 함수 안에서만 쓰일 큐

        while queue:
            [i, j] = queue.pop(0)
            block.append([i, j])  # 블록에 쌓아줌
            visited.append([i, j])  # 방문 리스트에 쌓아줌

            if house[i][j] == 1:  # 각각 상하좌우를 확인하는 조건문
                if i < N - 1 and house[i + 1][j] == 1 and [i + 1, j] not in block and [i + 1, j] not in queue:
                    queue.append([i + 1, j])
                if j < N - 1 and house[i][j + 1] == 1 and [i, j + 1] not in block and [i, j + 1] not in queue:
                    queue.append([i, j + 1])
                if j > 0 and house[i][j - 1] == 1 and [i, j - 1] not in block and [i, j - 1] not in queue:
                    queue.append([i, j - 1])
                if i > 0 and house[i - 1][j] == 1 and [i - 1, j] not in block and [i - 1, j] not in queue:
                    queue.append([i - 1, j])

        return [len(block), visited]  # 블록의 크기와, 방문한 노드들만 반환

    N = int(input())
    house = []
    visited = []
    result = []
    for _ in range(N):  # 단지를 2차원 배열로 받음
        house.append(list(map(int, str(input()))))

    # 0,0 부터 N,N까지 각각의 노드에 관하여 함수 실행
    for i in range(N):
        for j in range(N):
            if [i, j] not in visited:
                [size, visited] = bfs(house, i, j, N, visited)
                if size != 0:  # 1이 하나라도 포함된 사이즈 추가
                    result.append(size)

                    # 출력문
    print(len(result))
    for i in sorted(result):
        print(i)

def sol2():
    ans2 = np.zeros(apeach.shape, dtype=np.uint8)

    cur_label = 0
    for y in range(apeach.shape[0]):
        for x in range(apeach.shape[1]):
            # 방문 전
            if ans2[y, x] == 0 and apeach[y, x] != 0:
                cur_label += 1
                cnt = dfs(x, y, cur_label, apeach, ans2, apeach[y, x])
                print("영역 {0}의 값은 {1}이고 {2}칸입니다.".format(cur_label, apeach[y,x], cnt))
    print(ans2)




def sol3():
    ans3 = np.zeros(ice_case.shape, dtype=np.uint8)  # 똑같은 모양에 0으로만 채워진 것

    # ice 문제는 0과 1을 반대로 뒤집음
    # ==> 나의 dfs 함수는 1을 기준으로 처리하기 때문
    for y in range(ice_case.shape[0]):
        for x in range(ice_case.shape[1]):
            if ice_case[y, x] == 0:
                ice_case[y, x] = 1
            else:
                ice_case[y, x] = 0

    cur_label = 0

    for y in range(ice_case.shape[0]):
        for x in range(ice_case.shape[1]):
            # 값이 있는 셀이고, 아직 방문 안했다면
            if ice_case[y, x] == 1 and ans3[y, x] == 0:
                cur_label += 1
                dfs(x, y, cur_label, ice_case, ans3, 1)

    print("얼음은 {0}덩이입니다.".format(cur_label))

    print(ans3)
'''


def sol4():
    rows, cols = maze.shape
    ans4 = np.zeros(maze.shape, dtype=np.uint8)

    queue = [[0, 0]]
    ans4[0, 0] = 1

    # 우, 하, 좌, 상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        y, x = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or ny >= cols or ny >= rows:
                continue

            # 갈 수 있는 칸이고, 아직 안가봤으면
            if maze[ny, nx] == 1 and ans4[ny, nx] == 0:
                queue.append([ny, nx])
                ans4[ny, nx] = ans4[y, x] + 1

        print(ans4, "\n")

if __name__ == "__main__":
    # sol1()
    # sol2()
    # sol3()
    sol4()



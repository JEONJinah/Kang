import numpy as np

ice_case = np.array([[0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1],
                    [1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0]])



def dfs(cur_x, cur_y, label, src, ans):
    stack = [[cur_x, cur_y]]

    rows, cols = src.shape

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while stack:
        x, y = stack.pop()
        ans[y, x] = label

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 예외처리
            if nx < 0 or ny < 0 or nx >= cols or ny >= rows:
                continue

            if src[ny, nx] == 1 and ans[ny, nx] == 0:
                stack.append([nx, ny])


# def sol1():
#     dfs()


# def sol2():
#     dfs()


def sol3():
    ans3 = np.zeros(ice_case.shape, dtype=np.uint8)  # 똑같은 모양에 0으로만 채워진 것

    # ice 문제는 0과 1을 반대로 뒤집음
    # ==> 나의 dfs함수는 1을 기준으로 처리하기 때문
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
                dfs(x, y, cur_label, ice_case, ans3)

    print("얼음은 {0}덩이 입니다.".format(cur_label))
    print(ans3)



# def sol4():
#     dfs()


if __name__ == "__main__":
    sol3()

import numpy as np
import cv2 as cv


bin_img = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

def dfs(cur_x, cur_y, label):
    # 현재 위치를 스택에 넣고 시작
    # stack = []
    # stack.append[cur_x, cur_y] 이 두 줄을 합치면 아래 한 줄
    stack = [[cur_x, cur_y]]

    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    # 스택이 빌 때까지 돈다.
    while stack:
        x, y = stack.pop()
        # 하나를 꺼내서 방문 표시
        group_img[y, x] = label

        # 인접 픽셀에 방문 가능한 곳이 있다면 스택에 넣는다.
        # x-1, y-1 | x, y-1 | x+1, y-1
        # x-1, y   | x, y   | x+1, y
        # x-1, y+1 | x, y+1 | x+1, y+1
        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i] # if 문 8번 쓰기 싫어서 합침

            if next_x < 0 or next_x >= cols or next_y < 0 or next_y >= rows:
                continue

            # 이미지의 값이 있고, 방문전이면 스택에 push
            if bin_img[next_y, next_x] == 1 and group_img[next_y, next_x] == 0:
                stack.append([next_x, next_y])


if __name__ == "__main__":
    src = cv.imread("./image/yes.jpg")
    rows = bin_img.shape[0]
    cols = bin_img.shape[1]
    group_img = np.zeros((rows, cols))
    cur_label = 0

    for y in range(1, rows):
        for x in range(1, cols):
            if bin_img[y, x] == 1 and group_img[y, x] == 0:
                cur_label += 1
                dfs(x, y, cur_label)
           # 원본 이미지에서 값이 있는 경우
            if bin_img[y, x] == 1:
                # 좌측 혹은 상단 픽셀에 레이블이 되어있으면...
                if group_img[y, x-1] != 0 or group_img[y-1, x] != 0:
                    # 왼쪽에 값이 있으면 왼쪽 따라감
                    if group_img[y, x-1] != 0:
                        group_img[y, x] = group_img[y, x-1]
                    # 아니면 윗쪽 따라감
                    else:
                        group_img[y, x] = group_img[y-1, x]

                # 좌측 혹은 상단에 레이블이 되어있지 않으면
                else:
                    cur_label += 1
                    group_img[y, x] = cur_label

    print(group_img)

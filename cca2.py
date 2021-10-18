import numpy as np
import cv2 as cv

# def dfs(bin_img, group_img, cur_x, cur_y, label):
#     # 스택에 현재 좌표를 넣는다. 얘가 루트다.
#     stack = [[cur_x, cur_y]]
#
#     dx = [-1, 0, 1, -1, 1, -1, 0, 1]
#     dy = [-1, -1, -1, 0, 0, 1, 1, 1]
#
#     # 스택이 빌 때까지 돈다.
#     while stack:
#         x, y = stack.pop()
#         # 하나를 꺼내서 방문 표시
#         group_img[y, x] = label
#
#         # 인접 픽셀에 방문 가능한 곳이 있다면 스택에 넣는다. (8 방향)
#         # x-1, y-1 | x, y-1 | x+1, y-1
#         # x-1, y   | x, y   | x+1, y
#         # x-1, y+1 | x, y+1 | x+1, y+1
#         for i in range(8):
#             next_x = x + dx[i]
#             next_y = y + dy[i]  # if 문 8번 쓰기 싫어서 합침
#
#             if next_x < 0 or next_x >= cols or next_y < 0 or next_y >= rows:
#                 continue
#
#             # 이미지의 값이 있고, 방문전이면 스택에 push
#             if bin_img[next_y, next_x] != 0 and group_img[next_y, next_x] == 0:
#                 stack.append([next_x, next_y])


if __name__ == "__main__":
    src = cv.imread("./image/yes.jpg")
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    th, bin_img = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
    print(th)

    bin_img = 255 - bin_img

    n_blob, label_img, stats, centerroi = cv.connectedComponentsWithStats(bin_img)

    show_img = src.copy()

    for i in range(1, n_blob):
        x, y, w, h, area = stats[i]
        if area > 50:
            cv.rectangle(show_img, (x, y, w, h), (255, 0 ,255), thickness=2)

    cv.imshow("blob", show_img)

    # rows, cols = bin_img.shape
    # print(rows, cols)
    #
    # # group_img = np.zeros((rows, cols), dtype=np.uint8)
    # group_img = bin_img.copy()
    # cur_label = 0
    #
    # n_group, label_img = cv.connectedComponents(bin_img, labels=None, connectivity=8, ltype=cv.CV_16U)
    #
    # cv.imshow("opencvlabel", label_img)

    # for y in range(rows):
    #     for x in range(cols):
    #         if bin_img[y, x] != 0 and group_img[y, x] == 0:
    #             cur_label += 1
    #             # dfs(bin_img, group_img, x, y, cur_label)
    #             cv.floodFill(group_img, None, (x, y), cur_label)

    # colors = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [255, 0, 255], [0, 255, 255]]
    #
    # group_img = cv.cvtColor(group_img, cv.COLOR_GRAY2BGR)
    #
    # for y in range(rows):
    #     for x in range(cols):
    #         if label_img[y, x] != 0:
    #             colors_idx = label_img[y, x] % len(colors)
    #             group_img[y, x] = colors[colors_idx]

    cv.imshow("gray", gray)
    cv.imshow("bin", bin_img)
    cv.waitKey(0)
    cv.destroyWindow()

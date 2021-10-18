#  5/ 13 warming up
# def convolution (arr1, arr2):
#     sum = 0
#
#
#     if len(arr1) != len(arr2):
#         print("배열의 크기가 다릅니다.")
#         return -1
#
#     # for x in range(0, len(arr1)):
#     #     for y in range(0, len(arr2)):
#     #         sum += arr1[x][y] * arr2[x][y]
#
#     for y in range(len(arr1)):
#         for x in range(len(arr1[0])):
#             sum += arr1[y][x] * arr2[y][x]
#
#
#     return sum
#
# if __name__ == "__main__":
#     arr1 = [[1, 2, 3],
#            [6, 5, 4],
#            [7, 8, 9]]
#     arr2 = [[1, 0, 1],
#            [-1, 0, 1],
#            [2, 0, 2]]
#
#     con_val = convolution(arr1, arr2)
#     print(con_val)

# 5/ 13 그래디언트 사진 선따기
import cv2 as cv
import numpy as np

kernel_x = np.array([[1, 0, -1],
                     [2, 0, -2],
                     [1, 0, -1]])

kernel_y = np.array([[1, 2, 1],
                     [0, 0, 0],
                     [-1, -2, -1]])

gauss_filter = np.array([[1, 2, 1],
                         [2, 4, 2],
                         [1, 2, 1]])  # 그림 흐리게 하기기

if __name__ == "__main__":
    src = cv.imread("./image/building.jpg")
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    rows, cols = gray.shape
    gradient = np.zeros((rows-2, cols-2), dtype=np.uint8)
    g_x = np.zeros((rows - 2, cols - 2), dtype=np.uint8)
    g_y = np.zeros((rows - 2, cols - 2), dtype=np.uint8)

    for y in range(rows - 2):
        for x in range(cols - 2):
            roi = gray[y:y+3, x:x+3]
            gx = np.sum(gauss_filter * roi)
            gradient[y, x] = gx / 16

            # sx = np.sum(kernel_x * roi)  # 그래디언트
            # sy = np.sum(kernel_y * roi)
            # val = np.sqrt(sx**2 + sy**2)
            # if val > 200:
            #     gradient[y, x] = val
            # else:
            #     gradient[y, x] = 0


    cv.imshow("gray", gray)
    cv.imshow("gradient", gradient)
    cv.waitKey(0)
    cv.destroyWindow()

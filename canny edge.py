import cv2 as cv

if __name__ == "__main__":
    src = cv.imread("./image/lena.png", cv.IMREAD_GRAYSCALE)

    edge1 = cv.Canny(src, 50, 500)
    edge2 = cv.Canny(src, 80, 500)


    cv.imshow("edge1", edge1)
    cv.imshow("edge2", edge2)
    cv.waitKey(0)
    cv.destroyAllWindows()

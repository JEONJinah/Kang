import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    src = cv.imread("./image/test.png")
    # hist_src = np.bincount(src.ravel(), minlength=256)

    r_gray = src[:, :, 2]
    y_gray = src[:, :, 1]

    r_thr, r_bin = cv.threshold(r_gray, 0, 255, cv.THRESH_OTSU)
    print(r_thr)
    y_thr, y_bin = cv.threshold(r_gray, 0, 255, cv.THRESH_OTSU)
    print(y_thr)

    y_bin = cv.cvtColor(y_bin, cv.COLOR_GRAY2BGR)
    r_bin = cv.cvtColor(r_bin, cv.COLOR_GRAY2BGR)
    maked_img = cv.bitwise_and(src, y_bin)
    maked_img = cv.bitwise_and(maked_img, r_bin)


    # cv.imshow("y_gray", y_gray)
    # cv.imshow("r_gray", r_gray)
    #
    # roi = r_gray[87:168, 33:124]
    # cv.imshow("roi", roi)
    # histo = np.bincount(roi.ravel(), minlength=256)
    # plt.plot(histo)
    # plt.show()

    # norm_img = cv.normalize(src, None, 0, 255, cv.NORM_MINMAX)
    # cv.imshow("norm", norm_img)
    # hist_norm = np.bincount(norm_img.ravel(), minlength=256)
    #
    # equal_img = cv.equalizeHist(norm_img)
    # cv.imshow("equal", equal_img)
    # hist_equal = np.bincount(equal_img.ravel(), minlength=256)
    #
    # plt.subplot(1, 3, 1)
    # plt.plot(hist_src)
    #
    # plt.subplot(1, 3, 2)
    # plt.plot(hist_norm)
    #
    # plt.subplot(1, 3, 3)
    # plt.plot(hist_equal)
    # plt.show()
    #
    # # bin_img = equal_img.copy()
    # threshold = 100
    #
    # ret_val, bin_img = cv.threshold(r_gray, 0, 255, cv.THRESH_OTSU)
    # print(ret_val)
    #
    # # for y in range(equal_img.shape[0]):
    # #     for x in range(equal_img.shape[1]):
    # #         if equal_img[y,x]> threshold:
    # #             bin_img[y,x] = 255
    # #         else:
    # #             bin_img[y,x] = 0
    #
    # cv.imshow("bin img", bin_img)
    #
    cv.imshow("y_bin", y_bin)
    cv.imshow("r_bin", r_bin)
    cv.imshow("maked", maked_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    #

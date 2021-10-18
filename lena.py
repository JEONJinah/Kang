import cv2

if __name__ =='__main__':
  img = cv2.imread("./image/lena.png")
  cv2.imshow("Lena", img)
  cv2.waitKey(0)
  cv2.destroyWindow("Lena")

  cv2.ml

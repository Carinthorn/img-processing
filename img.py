import cv2

img = cv2.imread("img_processing/img/iris.jpeg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
img = cv2.flip(img, cv2.ROTATE_180)


cv2.imshow("BGR", img)
cv2.waitKey(-1)
cv2.destroyAllWindows()
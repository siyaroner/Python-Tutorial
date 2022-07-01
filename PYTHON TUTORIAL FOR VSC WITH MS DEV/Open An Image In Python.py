# from PIL import Image

# im = Image.open("C:/Users/TOSHIBA/Desktop/kitten.jpg")
import cv2
img= cv2.imread("./image/kitten.jpg")
cv2.imshow("kitten",img)
cv2.waitKey()

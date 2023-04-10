# A cartoon has 2 important characteristics:
# - Really clear edges
# - Homogeneous colours
# Starting from an original image taken from search engine
# I'm going to give to it a cartoon effect keeping in mind these 2 characteristics.
import cv2
import numpy as np

img = cv2.imread("Meyer.jpg")

# 1) Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 2) Color
color = cv2.bilateralFilter(img, 9, 300, 300)

# 3) Cartoon
cartoon = cv2.bitwise_and(color, color, mask=edges)


cv2.imshow("Image", img)
cv2.imshow("Cartoon", cartoon)
cv2.imshow("color", color)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
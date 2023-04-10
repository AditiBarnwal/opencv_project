import cv2
import numpy as np

img = cv2.imread("Meyer.jpg")

violet = (130, 0, 180)
pink = (255, 170, 100)
points = np.array([[[240, 250], [400, 280], [50, 250]]], np.int32)

cv2.ellipse(img, (250, 150), (100, 50), 0, 0, 360, violet, -1)
cv2.polylines(img, [points], True, pink, thickness=1)

cv2.imshow("ellipse", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

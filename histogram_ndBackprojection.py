import cv2
from matplotlib import pyplot

ori_img = cv2.imread("ikigaipng.png")
hsv_ori = cv2.cvtColor(ori_img, cv2.COLOR_BGR2HSV)

roi = cv2.imread("Ofkikai.png")
hsv_roi = cv2.cvtColor(ori_img, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(hsv_roi)

# histogram_roi
roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
mask = cv2.calcBackProject([hsv_ori], [0, 1], roi_hist, [0, 180, 0, 256], 1)

# filtering remove noise
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
#mask = cv2.filter2D(mask, -1, kernel)
#_, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)

#mask = cv2.merge((mask, mask, mask))
#result = cv2.bitwise_and(ori_img, mask)

cv2.imshow("Mask", mask)
cv2.imshow("Original image", ori_img)
#cv2.imshow("Result", result)
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

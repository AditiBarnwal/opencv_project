import cv2
import numpy as np

img = cv2.imread("ikigaipng.png")
roi = img[77:378, 170:380]
x = 170
y = 77
width = 380-x
height = 378-y
# to use camshift taking roi
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])

term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # back projection
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    ret, track_window = cv2.CamShift(mask, (x, y, width, height), term_criteria)
    print(ret)

    # for rectangle
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    cv2.polylines(frame, [pts], True, (255, 0, 0), 2)

    cv2.imshow("mask", mask)

    cv2.imshow("frame", frame)
    # cv2.imshow("ikigaipng", img)
    # cv2.imshow("roi", roi)

    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()

# i used my phone for ikigai cover in video and it worked ^^_

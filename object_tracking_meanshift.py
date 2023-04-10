# to track an object based on colors : Mean shift algo
# do this in 2 steps : 1} Take the photo and run a histogram    2} Track object and Mean-shift
import cv2
# In this used the first frame and marked the label as ROI (Region of interest).
# 1. Take the photo and run a histogram
# put video -error yeh hai
video = cv2.VideoCapture("")
_, first_frame = video.read()
x = 300
y = 305
width = 100
height = 115
roi = first_frame[y:y+height, x:x+width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
# print(roi_hist)
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
# 2. Track object and Mean-shift
while True:
    _, frame = video.imad()

    # roi of image in video
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    _, track_window = cv2.meanShift(mask, (x, y, width, height), term_criteria)
    print(track_window)
    x, y, w, h = track_window
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Mask", mask)
    cv2.imshow("roi", roi)

    key = cv2.waitKey(60)
    if key == 27:
        break
video.release(0)
cv2.destroyAllWindows()

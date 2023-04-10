# to distinguish the stable background from the objects that are moving.
# Keep in mind that this method only works with a stable camera and a stable background.

# On opencv we have two ways to subtract the background:
# 1} Manual subtraction from first frame
# 2} The SubtractorMOG2 which has more advanced features, like for example
#    keeping the history of last number of frames and detecting shadows.

import cv2
import numpy as np

cap = cv2.VideoCapture("highway.mp4")
_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_grey = cv2.GaussianBlur(first_gray, (5, 5), 0)
while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    difference = cv2.absdiff(first_gray, gray_frame)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

    cv2.imshow("first_frame", first_frame)
    cv2.imshow("frame", frame)
    cv2.imshow("difference", difference)

    key = cv2.waitKey(33)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()


# core part of the background subtraction where we compute the absolute
# difference between the first frame and the current frame we are in inside the loop.

# The Subtractor MOG2, is already built in Opencv, and it’s simpler to use than the manual mode.
# Why is working with a frame history an advantage?

# Let’s consider that take the first frame of a highway during the day,
# after a few hours when the sun goes down, computing the difference from the
# first frame taken a few hours before would not work, the images on the day
# and night will be completely different.
# Working with the frame history don’t have this problem.

# load libraries and video.
import cv2
import numpy as np
cap = cv2.VideoCapture("highway.mp4")

# load subtractor
# Inside the parenthesis we can change the value of the subtractor. History is the number
# of the last frame that are taken into consideration (by default 120).
# The threshold value is the value used when computing the difference to extract the background.
# A lower threshold will find more differences with the advantage of a more noisy image.
# Detect-shadows is a function of the algorythm that can remove the shadows if enabled.
# There are no right or wrong values, you need to try different settings to see what best fits your need.
#
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

# then run the while loop to get the frames from the video.

while True:
    _, frame = cap.read()
    # Once we have the frames we can use the subtractor to find get the background.
    mask = subtractor.apply(frame)
    # show everything on the screen.
    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(30)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
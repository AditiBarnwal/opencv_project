# to find feature on image : use SIFT, SURF, ORB algos
# SURF & SIFT detect more features than ORB, but ORB is faster
# install opencv-contrib-python
import cv2
import numpy as np

img = cv2.imread("imagesdownload.png", cv2.IMREAD_GRAYSCALE)
# load one by one above algos
sift = cv2.xfeatures2d.SIFT_create()
# surf = cv2.xfeatures2d.SURF_create()
orb = cv2.ORB_create(nfeatures=1500)

# for each algo find keypoints & descriptor
# Keypoints : the postion where feature has been detected.
# Descriptor : is an array containing numbers to describe the features.

# When the descriptors are similar, it means that also the feature is similar.
keypoints_sift, descriptors = sift.detectAndCompute(img, None)
# keypoints_surf, descriptors = surf.detectAndCompute(img, None)
keypoints_orb, descriptors = orb.detectAndCompute(img, None)

img = cv2.drawKeypoints(img, keypoints_orb, None)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Detection done now matching to real video : refer to "feature matching"

import cv2
import numpy as np

original = cv2.imread("images/original_golden_bridge.jpg")
image_to_compare = cv2.imread("images/george-washington-bridge.jpg")

# 1) Check if 2 images are equals
if original.shape == image_to_compare.shape:
    print("The images have same size and channels")
    difference = cv2.subtract(original, image_to_compare)
    b, g, r = cv2.split(difference)

    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")
    else:
        print("The images are NOT equal")

# 2) Check for similarities between the 2 images

sift = cv2.xfeatures2d.SIFT_create()
kp_1, desc_1 = sift.detectAndCompute(original, None)
kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

# load FlannBasedMatcher which is the method used to find the matches between the descriptors of the 2 images.
index_params = dict(algorithm=0, trees=5)
search_params = dict()  # the matches between the 2 images. We’re storing the matches in the array ‘matches’.
flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(desc_1, desc_2, k=2)

# apply the ratio test to select only the good matches.
# The quality of a match is define by the distance. The distance is a number,
# and the lower this number is, the more similar the features are.
# By applying the ratio test we can decide to take only the matches with lower distance, so higher quality.
#
# If you decrease the ratio value, for example to 0.1 you will get really high quality matches,
# but the downside is that you will get only few matches.
# If you increase it you will get more matches but sometimes many false ones.

good_points = []
ratio = 0.6

for m, n in matches:

    if m.distance < ratio * n.distance:
        good_points.append(m)

print(len(good_points))
result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)

cv2.imshow("result", cv2.resize(result, None, fx=0.4, fy=0.4))
cv2.imshow("Original", cv2.resize(original, None, fx=0.4, fy=0.4))
cv2.imshow("Duplicate", cv2.resize(image_to_compare, None, fx=0.4, fy=0.4))
cv2.waitKey(0)
cv2.destroyAllWindows()

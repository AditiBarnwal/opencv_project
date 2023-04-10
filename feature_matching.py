# for object matching placing object in different lighting condition, position & perspective
# characterstics compared with two methods: 1} orb detector method  2}Brute force matching
import cv2
import numpy

img1 = cv2.imread("ikigaipng.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("imagesdownload.png", cv2.IMREAD_GRAYSCALE)

# Orb detector method
# Passing the image to the ORB Detector method we obtain an array with the definition of the image characteristics.
# Obviously it will not do the pixel by pixel analysis because obviously they will be different.
# ORB Detector
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)


# Brute Force Matching
# For this purpose we use the BFMatcher opencv method. Here are some parameters to set:
#
# Norm_hamming : is used when comparing Orb detector arrays
# crosscheck = true : it allows us to have only the results with the best score in the comparison

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

# Finally we draw the lines that represent the equalities:

matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None, flags=2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("matching", matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()


# {I do not recommend using this method for real-time analysis,
# such as a video, because it requires a lot of computing energy}

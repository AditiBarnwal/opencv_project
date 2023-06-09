# How work Optical Flow?
# Optical flow is the vector who describe the movement of the object between two consecutive frames.
# The Lucas-Kanade algorithm needs some conditions to work. For example, the object must move really close,
# no matter if it is fast because the algorithm analyzes frame by frame.

#  To retrieve the data frame by frame from the camera.
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# create old_frame
_, frame = cap.read()
old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Lucas kanade params
lk_params = dict(winSize=(10, 10),
                 maxLevel=4, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))


# mouse func
def select_point(event, x, y, flags, paras):
    global point, point_selected, old_points
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x, y)
        point_selected = True
        old_points = np.array([[x, y]], dtype=np.float32)

# to run func in frame
cv2.namedWindow("frame")
cv2.setMouseCallback("frame", select_point)

point_selected = False
point = ()
old_points = np.array([[]])

while True:
    _, frame = cap.read()
    #  Now calcOpticalFlowPyrLK () tracking function.
    #  convert the frame to grayscale format.
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # for point in frame
    if point_selected is True:
        cv2.circle(frame, point, 5, (0, 255, 0), 2)
        new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame, old_points, None, **lk_params)
        old_gray = gray_frame.copy()
        old_points = new_points
        x, y = new_points.ravel()
        cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

    # first_level = cv2.pyrDown(frame)
    # second_level = cv2.pyrDown(first_level)

    cv2.imshow("frame", frame)
    # cv2.imshow("first_frame", first_level)
    # cv2.imshow("second_frame", second_level)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

# parameters used in the optical-flow function:

# 1. old_gray : old frame array
# 2. gray_frame : current frame
# 3. old_point : array with old point
# 4. None : empy param
# 5. **lk_params : some configuration about the function

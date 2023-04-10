# Mouse events can be left-button down, left-button up, double-click, etc.
# It gives us the coordinates (x,y) for every mouse event.
# setMouseCallback : function is called whenever the mouse is moved or a button is used.

# When calling setMouseCallback you don't CALL draw_circle, but you tell setMouseCallback which
# function should be called on a mouse event (that's called a callback function).
import cv2
drawing = False
pt1 = ()
pt2 = ()


def mouse_drawing(event, x, y, flags, paras):
    global pt1, pt2, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        print("left click")
        circles.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        if drawing is False:
            drawing = True
            pt1 = (x, y)
        else:
            drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            pt2 = (x, y)

cap = cv2.VideoCapture(0)

cv2.namedWindow("frame")
cv2.setMouseCallback("frame", mouse_drawing)
circles = []

while True:
    _, frame = cap.read()

    if circles:
        for center_pos in circles:
            cv2.circle(frame, center_pos, 5, (100, 200, 255), -1)
    elif pt1 and pt2:
        cv2.rectangle(frame, pt1, pt2, (190, 255, 69))

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("f"):
        circles = []
cap.release()
cv2.destroyAllWindows()

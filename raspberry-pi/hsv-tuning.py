import cv2
import numpy as np

def nothing(x):
    pass

# Create window
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 400, 300)

# Create HSV trackbars for lower and upper bounds
cv2.createTrackbar("Lower H", "Trackbars", 5, 179, nothing)
cv2.createTrackbar("Lower S", "Trackbars", 100, 255, nothing)
cv2.createTrackbar("Lower V", "Trackbars", 100, 255, nothing)

cv2.createTrackbar("Upper H", "Trackbars", 25, 179, nothing)
cv2.createTrackbar("Upper S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Upper V", "Trackbars", 255, 255, nothing)

# Start camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get current trackbar positions
    l_h = cv2.getTrackbarPos("Lower H", "Trackbars")
    l_s = cv2.getTrackbarPos("Lower S", "Trackbars")
    l_v = cv2.getTrackbarPos("Lower V", "Trackbars")
    u_h = cv2.getTrackbarPos("Upper H", "Trackbars")
    u_s = cv2.getTrackbarPos("Upper S", "Trackbars")
    u_v = cv2.getTrackbarPos("Upper V", "Trackbars")

    # Create masks
    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Show images
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Filtered", result)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np

# Load image
image = cv2.imread(r"C:\Users\asus\Downloads\color.png")

if image is None:
    print("Error: Image not found!")
    exit()

# Resize image if it is too large
max_width = 1000
max_height = 700

height, width = image.shape[:2]
scale = min(max_width / width, max_height / height)

if scale < 1:
    image = cv2.resize(image, None, fx=scale, fy=scale)

# Keep a copy for drawing
result = image.copy()

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV ranges for each color
colors = {

    "Red": [
        (np.array([0, 120, 70]), np.array([10, 255, 255])),
        (np.array([170, 120, 70]), np.array([180, 255, 255]))
    ],

    "Blue": [
        (np.array([100, 150, 50]), np.array([140, 255, 255]))
    ],

    "Green": [
        (np.array([40, 70, 70]), np.array([80, 255, 255]))
    ],

    "Yellow": [
        (np.array([20, 100, 100]), np.array([35, 255, 255]))
    ],

    "Purple": [
        (np.array([125, 50, 50]), np.array([155, 255, 255]))
    ],

    "Black": [
        (np.array([0, 0, 0]), np.array([180, 255, 50]))
    ]  
}

kernel = np.ones((5, 5), np.uint8)

# Detect colors
for color_name, ranges in colors.items():

    mask = np.zeros(hsv.shape[:2], dtype=np.uint8)

    for lower, upper in ranges:
        mask |= cv2.inRange(hsv, lower, upper)

    # Remove small noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:

        if cv2.contourArea(contour) < 500:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(
            result,
            color_name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

# Show result
cv2.namedWindow("Color Recognition", cv2.WINDOW_NORMAL)
cv2.imshow("Color Recognition", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
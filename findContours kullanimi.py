import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

matlike = np.array([
    [0,0,0,255,0,0,0],
    [0,0,4,0,0,0,0],
    [0,4,0,0,0,0,0],
    [255,0,0,0,255,0,0],
    [0,4,0,0,0,0,0],
    [0,0,255,0,0,0,0],
    [0,0,0,4,0,0,0]
], dtype=np.uint8)

# Scale each pixel by 8 × 8
matlike = cv.resize(
    matlike,
    None,
    fx=8,
    fy=8,
    interpolation=cv.INTER_NEAREST
)

# Find contours on the grayscale image
contours, _ = cv.findContours(
    matlike,
    cv.RETR_EXTERNAL,
    cv.CHAIN_APPROX_SIMPLE
)

# Convert to color so contours can be green
contoured = cv.cvtColor(matlike, cv.COLOR_GRAY2BGR)

cv.drawContours(
    contoured,
    contours,
    -1,
    (0, 255, 0),
    1
)

plt.imshow(cv.cvtColor(contoured, cv.COLOR_BGR2RGB))
plt.show()

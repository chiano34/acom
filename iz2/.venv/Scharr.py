import cv2
import numpy as np
def scharr_filter(image):
    scharr_x = np.array([[3, 0, -3],
                         [10, 0, -10],
                         [3, 0, -3]])

    scharr_y = np.array([[3, 10, 3],
                         [0, 0, 0],
                         [-3, -10, -3]])

    gradient_x = cv2.filter2D(image.astype(np.float32), -1, scharr_x)
    gradient_y = cv2.filter2D(image.astype(np.float32), -1, scharr_y)
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

    return gradient_magnitude
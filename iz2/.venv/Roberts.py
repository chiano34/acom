
import cv2
import numpy as np

def gaussian_blur(image, kernel_size=5, sigma=1.0):
    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    kernel = kernel * kernel.T  # Создание 2D гауссового ядра
    return cv2.filter2D(image, -1, kernel)

def roberts_gradient(image):
    roberts_x = np.array([[1, 0],
                          [0, -1]])

    roberts_y = np.array([[0, 1],
                          [-1, 0]])

    gradient_x = cv2.filter2D(image.astype(np.float32), -1, roberts_x)
    gradient_y = cv2.filter2D(image.astype(np.float32), -1, roberts_y)

    magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    direction = np.arctan2(gradient_y, gradient_x) * (180 / np.pi) % 180

    return magnitude, direction

def non_maximum_suppression(magnitude, direction):
    height, width = magnitude.shape
    suppressed = np.zeros_like(magnitude)

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            angle = direction[i, j]
            if (angle < 22.5 or angle >= 157.5):  # горизонтальные границы
                neighbors = [magnitude[i, j + 1], magnitude[i, j - 1]]
            elif (22.5 <= angle < 67.5):  # диагональные границы
                neighbors = [magnitude[i + 1, j + 1], magnitude[i - 1, j - 1]]
            elif (67.5 <= angle < 112.5):  # вертикальные границы
                neighbors = [magnitude[i + 1, j], magnitude[i - 1, j]]
            else:  # диагональные границы
                neighbors = [magnitude[i + 1, j - 1], magnitude[i - 1, j + 1]]

            if (magnitude[i, j] >= max(neighbors)):
                suppressed[i, j] = magnitude[i, j]

    return suppressed

def double_threshold(suppressed_image, low, high):
    strong_edges = (suppressed_image > high)
    weak_edges = ((suppressed_image >= low) & (suppressed_image <= high))

    return strong_edges.astype(np.uint8), weak_edges.astype(np.uint8)

def filter(strong_edges, weak_edges):
    height, width = strong_edges.shape
    output_image = np.zeros_like(strong_edges)

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if strong_edges[i,j]:
                output_image[i,j] = 255
            elif weak_edges[i,j]:
                if ((strong_edges[i+1,j] or strong_edges[i-1,j] or
                     strong_edges[i,j+1] or strong_edges[i,j-1] or
                     strong_edges[i+1,j+1] or strong_edges[i-1,j-1] or
                     strong_edges[i+1,j-1] or strong_edges[i-1,j+1])):
                    output_image[i,j] = 255

    return output_image
def main(image_path,kernel,sigma,low,high):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_image, (kernel,kernel), sigma)
    magnitude, direction = roberts_gradient(blurred)
    suppressed_image = non_maximum_suppression(magnitude, direction)
    strong_edges, weak_edges = double_threshold(suppressed_image,low, high)
    final_edges = filter(strong_edges, weak_edges)
    return  final_edges
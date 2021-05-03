import cv2
import matplotlib.pyplot as plt
import numpy as np
from desmos import start_plot
from solver import Solver


def plot_image(img):
    plt.imshow(img, cmap='binary')
    plt.show()


def get_contours(img_path):
    image = cv2.imread('Itachi.jpeg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 200)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours, image


def filter_countours(contours, threshold):
    result = []
    for contour in contours:
        if len(contour) > threshold:
            result.append(contour)
    return result

if __name__ == "__main__":
    contours, image = get_contours("Itachi.jpeg")
    contours = filter_countours(contours, 1500)

    # mask = np.zeros(image.shape)
    # cv2.drawContours(mask, contours, -1, (0, 255, 0), 1)
    # print("Showing Contours")
    # cv2.imshow("Contours", mask)
    # cv2.waitKey(0)

    print("Solving Contours")

    solver = Solver(contours)
    solver.solve()
    print("Solved")
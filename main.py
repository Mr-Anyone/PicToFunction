import cv2
import matplotlib.pyplot as plt
import numpy as np
import shutil
import os
from solver import Solver


def plot_image(img):
    plt.imshow(img, cmap='binary')
    plt.show()


def get_contours(img_path):
    image = cv2.imread(img_path)
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

def init():
    try:
        shutil.rmtree(os.path.join(os.curdir, "Equations"))
    except Exception as e:
        pass

if __name__ == "__main__":
    init()
    contours, image = get_contours("Logo.jpeg")
    contours = filter_countours(contours, 10)

    # mask = np.zeros(image.shape)
    # cv2.drawContours(mask, contours, -1, (0, 255, 0), 1)
    # print("Showing Contours")
    # cv2.imshow("Contours", mask)
    # cv2.waitKey(0)

    print("Solving Contours")

    solver = Solver(contours)
    solver.solve(max_equations=500)
    print("Solved")
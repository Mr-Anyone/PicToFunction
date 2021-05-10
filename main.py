import cv2
import matplotlib.pyplot as plt
import numpy as np
import shutil
import os
from solver import Solver

MAX_EQ = 1000
IMG_NAME = "David.jpeg"
FILTER_COUNT = 100

def plot_image(img):
    plt.imshow(img, cmap='binary')
    plt.show()


def get_contours(img_path):
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 200)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours, image


def filter_contours(contours, threshold):
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

def draw_contours(image, contours):
    mask = np.zeros(image.shape)
    cv2.drawContours(mask, contours, -1, (0, 255, 0), 1)
    return mask

if __name__ == "__main__":
    init()
    contours, image = get_contours(IMG_NAME)
    contours = filter_contours(contours, FILTER_COUNT)

    mask = draw_contours(image, contours)
    print("Showing Contours")
    print(f"Total of : {len(contours)}")
    cv2.imshow("Contours", mask)
    cv2.waitKey(0)

    print("Solving Contours")
    height, width, _ = image.shape
    solver = Solver(contours, width, height)
    solver.solve(max_equations=MAX_EQ)
    print("Solved")
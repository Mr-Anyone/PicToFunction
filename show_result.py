from main import IMG_NAME, get_contours, filter_contours, FILTER_COUNT, draw_contours
import cv2
import numpy as np
import pickle
import os

def load_object(path):
    f = open(path, 'rb')
    return pickle.load(f)

def draw_result(image):
    save_dir = os.path.join(os.curdir, "Equations")
    height, width, _ = image.shape
    mask = np.zeros((height, width))

    for file in os.listdir(save_dir):
        if "DS_STORE" not in file:
            filepath = os.path.join(save_dir, file)
            obj = load_object(filepath)
            point1, point2 = obj.show_result_data()
            x1, y1 = point1
            x2, y2 = point2
            y1, y2 = int(height - y1), int(height - y2)
            mask = cv2.line(mask, (x1, y1), (x2, y2), (255, 255, 255), 1)
    return mask


if __name__ == "__main__":
    contours, image = get_contours(IMG_NAME)
    contours = filter_contours(contours, FILTER_COUNT)
    mask = draw_contours(image, contours)

    result_img = draw_result(image)
    cv2.imshow("Result Image", result_img)
    cv2.imshow("Contours", mask)
    cv2.imshow("Image", image)
    cv2.waitKey(0)


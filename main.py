import matplotlib.pyplot as plt
import cv2

def solver():
    return "Hello World"


def plot_image(img):
    plt.imshow(img, cmap='binary')
    plt.show()

def get_contours(img_path):
    image = cv2.imread('Itachi.jpeg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 200)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours, image

if __name__ == "__main__":
    contours, image = get_contours("Itachi.jpeg")
    short_line = 50 # Small that this values means this is a short line
    print(len(contours), type(contours))
    real_stuff = []

    for contour in contours:
        if len(contour) > short_line:
            real_stuff.append(contour)
    cv2.drawContours(image, real_stuff[:10], -1, (0, 255, 0), 1)
    cv2.imshow("Contours",image)
    cv2.waitKey(0)
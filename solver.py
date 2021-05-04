from Equations import *

def transform_mapping(y, img_height):
    return img_height - y

class Solver():
    def __init__(self, contours, img_width, img_height):
        self.contours = contours
        self.img_width = img_width
        self.img_height = img_height

    def solve(self, max_equations=100):
        point_count = number_of_points(self.contours) # Number of points in contour
        for contour in self.contours:
            loop_per_instance = int(max_equations * len(contour)/ point_count)
            if loop_per_instance != 0:
                split_ratio = int(len(contour) / loop_per_instance)
            else:
                split_ratio = 0

            for i in range(loop_per_instance):
                try:
                    start_point = contour[i * split_ratio]
                    x1, y1 = start_point[0][0], start_point[0][1]
                    y1 = transform_mapping(y1, self.img_height)

                    if (i + 1) * split_ratio >= len(contour):
                        end_point = contour[-1]
                    else:
                        end_point = contour[(i + 1) * split_ratio]

                    x2, y2 = end_point[0][0], end_point[0][1]
                    y2 = transform_mapping(y2, self.img_height)

                    if x1 - x2 != 0:
                        k = (y1 - y2) / (x1 - x2)  # The slope of the line
                        b = y1 - (k * x1)  # The line offset

                        equation = LinearEquations(k, b, x1, x2)
                        equation.save()
                    else:
                        equation = VerticalLine(x1, y1, y2)
                        equation.save()


                except Exception as e:
                    print(f"Error: {e}")

def number_of_points(contours):
    points = 0
    for contour in contours:
        points += contour.shape[0]
    return points

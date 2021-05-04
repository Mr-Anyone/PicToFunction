from Equations import *


class Solver():
    def __init__(self, contours):
        self.contours = contours

    def solve(self, max_equations=100):
        equations_per_contour = int(max_equations / len(self.contours))
        if equations_per_contour == 0:
            equations_per_contour = 1

        for contour in self.contours:
            split_ratio = int(len(contour) / equations_per_contour)

            for i in range(equations_per_contour):
                try:
                    start_point = contour[i * split_ratio]
                    x1, y1 = start_point[0][0], start_point[0][1]

                    if (i + 1) * split_ratio >= len(contour):
                        end_point = contour[-1]
                    else:
                        end_point = contour[(i + 1) * split_ratio]

                    x2, y2 = end_point[0][0], end_point[0][1]

                    if x1 - x2 != 0:
                        k = (y1 - y2) / (x1 - x2)  # The slope of the line
                        b = y1 - (k * x1)  # The line offset

                        equation = LinearEquations(k, b, x1, x2)
                        equation.save()
                    else:
                        print("Vertical Line")
                        equation = VerticalLine(x1, y1, y2)
                        equation.save()


                except Exception as e:
                    print(f"Error: {e}")


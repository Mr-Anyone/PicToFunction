import os
import pickle


class Solver():
    def __init__(self, contours):
        self.contours = contours

    def solve(self, max_equations=100):
        equations_per_contour = int(max_equations/len(self.contours))
        if equations_per_contour == 0:
            equations_per_contour = 1

        for contour in self.contours:
            split_ratio = int(len(contour) / equations_per_contour)

            for i in range(equations_per_contour):
                try:
                    start_point = contour[i * split_ratio]
                    x1, y1 = start_point[0][0], start_point[0][1]
                    end_point = contour[(i+1) * split_ratio]
                    x2, y2 = end_point[0][0], end_point[0][1]

                    if x1-x2 != 0:
                        k = (y1-y2)/(x1-x2)# The slope of the line
                        b = y1 - (k*x1) # The line offset

                        equation = LinearEquations(k, b, x1, x2)
                        equation.save()
                except Exception as e:
                    print(f"Error: {e}")

class LinearEquations():
    save_dir = os.path.join(os.curdir, "Equations")

    def __init__(self, k, b, x1, x2, save=False):
        self.k = k
        self.b = b
        self.x1 = x1
        self.x2 = x2

        if save:
            self.save()

    def save(self):
        self.mkdir(self.save_dir)
        with open(os.path.join(self.save_dir, f"f(x) = {self.k}x + {self.b} {self.x1} {self.x2}.pickle"), 'wb') as f:
            pickle.dump(self, f)

    def mkdir(self, path):
        try:
            os.mkdir(path)
        except Exception as e:
            pass

    def get_desmos_domain(self):
        """
        Return the domain of the graph
        :return: smaller point, larger point
        """
        if self.x1 > self.x2:
            return self.x2, self.x1
        else:
            return self.x1, self.x2

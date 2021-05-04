import os
import pickle


class Equation():
    save_dir = os.path.join(os.curdir, "Equations")

    def __init__(self, filename):
        self.filename = filename

    def save(self):
        self.mkdir(self.save_dir)
        with open(os.path.join(self.save_dir, self.filename), 'wb') as f:
            pickle.dump(self, f)

    def mkdir(self, path):
        try:
            os.mkdir(path)
        except Exception as e:
            pass


class LinearEquations(Equation):
    save_dir = os.path.join(os.curdir, "Equations")

    def __init__(self, k, b, x1, x2, save=False):
        self.k = k
        self.b = b
        self.x1 = x1
        self.x2 = x2
        super(LinearEquations, self).__init__(f"f(x) = {self.k}x + {self.b} {self.x1} {self.x2}.pickle")
        if save:
            self.save()

    def get_desmos_domain(self):
        """
        Return the domain of the graph
        :return: smaller point, larger point
        """
        if self.x1 > self.x2:
            return self.x2, self.x1
        else:
            return self.x1, self.x2

    def write_function(self):
        x1, x2 = self.get_desmos_domain()
        return f"f(x) = {self.k}x + {self.b} " + r"{ " + f"{x1} <= x <= {x2}" + r"}"


class VerticalLine(Equation):
    def __init__(self, line_x, y1, y2, save=True):
        super().__init__(f"{line_x} {y1} {y2}.pickle")
        self.line_x = line_x
        self.y1 = y1
        self.y2 = y2

        if save:
            self.save()

    def get_domain(self):
        if self.y1 > self.y2:
            return self.y2, self.y1
        else:
            return self.y1, self.y2

    def write_function(self):
        y1, y2 = self.get_domain()
        return f" x = {self.line_x} " + r"{" + f"{y1}<= y <= {y2}" + "}"

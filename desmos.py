import os
import pickle
import time
from pynput.keyboard import Controller, Key

save_dir = os.path.join(os.curdir, "Equations")


def load_object(filename):
    f = open(os.path.join(save_dir, filename), 'rb')
    return pickle.load(f)


def write_function(obj, x1, x2):
    return f"f(x) = {obj.k}x + {obj.b} " + r"{" + f"{x1} <= x <= {x2}" + r"}"


def start_plot(delay=1):
    keyboard = Controller()  # The keyboard controlling class
    time.sleep(10)
    for filename in os.listdir(save_dir):
        if ".pickle" in filename:  # Prevent .DS_Store from loading
            obj = load_object(filename)
            x1, x2 = obj.get_desmos_domain()
            function_string = write_function(obj, x1, x2)

            keyboard.type(function_string)
            keyboard.press(Key.enter)
            time.sleep(delay)


if __name__ == "__main__":
    start_plot()

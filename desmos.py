import os
import pickle
import time
from pynput.keyboard import Controller, Key, Listener

save_dir = os.path.join(os.curdir, "Equations")
run = False


def load_object(filename):
    f = open(os.path.join(save_dir, filename), 'rb')
    return pickle.load(f)


def write_function(obj, x1, x2):
    return f"f(x) = {obj.k}x + {obj.b} " + r"{" + f"{x1} <= x <= {x2}" + r"}"


def start_plot(delay=1):
    global run

    keyboard = Controller()  # The keyboard controlling class
    for filename in os.listdir(save_dir):
        if run:
            if ".pickle" in filename:  # Prevent .DS_Store from loading
                obj = load_object(filename)
                function_string = obj.write_function()

                keyboard.type(function_string)
                keyboard.press(Key.enter)
                time.sleep(delay)
                obj.remove()
        else:
            break


def on_press(key):
    global run
    if key == Key.alt_r:
        print("Started")
        run = True
    elif key == Key.alt_l:
        print("Stopped")
        run = False


def on_release(key):
    pass


if __name__ == "__main__":
    listener = Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    while True:
        start_plot()

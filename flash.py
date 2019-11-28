import json
from time import sleep
import sys

def light():
    with open("/sys/class/leds/input4::capslock/brightness", 'w') as f:
        f.write('1')


def dark():
    with open("/sys/class/leds/input4::capslock/brightness", 'w') as f:
        f.write('0')

with open("./morse.json", 'r') as f:
    morse = json.load(f)

try:
    text = sys.argv[1].lower()
except:
    print("Usege: python3 flash.py \"message\"")

keys = morse.keys()

for ch in text:
    if (ch not in keys):
        continue
    for c in morse[ch]:
        if c == '.':
            light()
            sleep(0.2)
            dark();
        elif c == '-':
            light()
            sleep(1)
            dark()
        sleep(0.5)

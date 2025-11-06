import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

SHORT_DELAY = 0.5
MEDIUM_DELAY = 0.75
SEARCH_DELAY = 1.0
APP_LAUNCH_DELAY = 3.0
TILING_DELAY = 1.0

GUI = Keycode.GUI
ALT = Keycode.ALT
CONTROL = Keycode.CONTROL

print("Starting CircuitPython workflow script...")

time.sleep(4.0)

kbd.send(GUI, Keycode.SPACE)
time.sleep(SHORT_DELAY)
kbd.write("Spotify")
time.sleep(SEARCH_DELAY)
kbd.send(Keycode.ENTER)
time.sleep(APP_LAUNCH_DELAY)

kbd.send(GUI, Keycode.K)
time.sleep(MEDIUM_DELAY)
kbd.write("pyari")
time.sleep(SEARCH_DELAY)
kbd.send(Keycode.ENTER)
time.sleep(2.5)

kbd.send(GUI, Keycode.SPACE)
time.sleep(SHORT_DELAY)
kbd.write("capcut")
time.sleep(SEARCH_DELAY)
kbd.send(Keycode.ENTER)
time.sleep(APP_LAUNCH_DELAY + 1.0)

kbd.send(GUI, Keycode.SPACE)
time.sleep(SHORT_DELAY)
kbd.write("http://adobe.com")
time.sleep(SEARCH_DELAY)
kbd.send(Keycode.ENTER)
time.sleep(APP_LAUNCH_DELAY)

kbd.send(CONTROL, ALT, GUI, Keycode.RIGHT_ARROW)
time.sleep(TILING_DELAY)

kbd.send(GUI, Keycode.TAB)
time.sleep(TILING_DELAY)

kbd.send(CONTROL, ALT, GUI, Keycode.LEFT_ARROW)
time.sleep(TILING_DELAY)

print("Workflow complete.")

while True:
    pass

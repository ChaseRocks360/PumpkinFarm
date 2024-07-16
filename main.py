import time
import ctypes
from PIL import ImageGrab
import win32api
import win32con

# Function to capture the screen
def capture_screen():
    screenshot = ImageGrab.grab()
    return screenshot

# Function to check for the specific orange color
def contains_orange_block(image, target_color=(224, 136, 29)):
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            if pixels[x, y][:3] == target_color:  # Compare only RGB values
                return True
    return False

# Initialize variables
no_orange_block_time = 0
last_checked = time.time()

while True:
    image = capture_screen()

    if contains_orange_block(image):
        no_orange_block_time = 0
    else:
        no_orange_block_time += 1

    if no_orange_block_time >= 5:
        # Press F8
        win32api.keybd_event(win32con.VK_F8, 0, 0, 0)
        win32api.keybd_event(win32con.VK_F8, 0, win32con.KEYEVENTF_KEYUP, 0)
        no_orange_block_time = 0  # Reset the timer after pressing F8

    # Check the screen every second
    while time.time() - last_checked < 1:
        time.sleep(0.01)
    last_checked = time.time()

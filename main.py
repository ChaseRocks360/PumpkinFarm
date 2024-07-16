import time
from PIL import ImageGrab
import win32api
import win32con
import pyautogui
import keyboard  # Import the keyboard library

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

# Main loop
while True:
    if keyboard.is_pressed('F7'):  # Check if F7 is pressed to stop the script
        print("F7 pressed. Exiting script.")
        break

    image = capture_screen()

    if contains_orange_block(image):
        no_orange_block_time = 0
    else:
        no_orange_block_time += 1

    if no_orange_block_time >= 5:
        # Wait 5 seconds
        time.sleep(5)

        # Press "T" key
        pyautogui.press('t')

        # Type "/garden"
        pyautogui.typewrite('/garden')
        pyautogui.press('enter')

        # Press F8 to stop the macro
        win32api.keybd_event(win32con.VK_F8, 0, 0, 0)
        win32api.keybd_event(win32con.VK_F8, 0, win32con.KEYEVENTF_KEYUP, 0)

        # Wait 2 seconds
        time.sleep(2)

        # Press F8 again to start the macro
        win32api.keybd_event(win32con.VK_F8, 0, 0, 0)
        win32api.keybd_event(win32con.VK_F8, 0, win32con.KEYEVENTF_KEYUP, 0)

        # Reset the timer after typing the command and pressing F8
        no_orange_block_time = 0

    # Check the screen every second
    while time.time() - last_checked < 1:
        if keyboard.is_pressed('F7'):  # Check again if F7 is pressed while waiting
            print("F7 pressed. Exiting script.")
            break
        time.sleep(0.01)
    last_checked = time.time()

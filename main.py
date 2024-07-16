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

# Function to simulate pressing a key
def press_key(key_code):
    win32api.keybd_event(key_code, 0, 0, 0)
    time.sleep(0.1)  # Add a small delay to ensure key press is registered
    win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

# Initialize variables
no_orange_block_start_time = None
last_checked = time.time()

# Main loop
while True:
    if keyboard.is_pressed('F7'):  # Check if F7 is pressed to stop the script
        print("F7 pressed. Exiting script.")
        break

    image = capture_screen()

    if contains_orange_block(image):
        no_orange_block_start_time = None  # Reset the start time if orange is detected
    else:
        if no_orange_block_start_time is None:
            no_orange_block_start_time = time.time()  # Start the timer if not already started
        else:
            if time.time() - no_orange_block_start_time >= 5:  # Check if 5 seconds have passed
                print("No orange block detected for 5 seconds. Pressing F8 to start the macro.")

                # Press F8 to stop the macro
                press_key(win32con.VK_F8)

                # Wait 2 seconds to ensure F8 key press is registered
                time.sleep(2)

                # Press "T" key
                pyautogui.press('t')

                # Type "/garden"
                pyautogui.typewrite('/garden')
                pyautogui.press('enter')

                # Wait 2 seconds
                time.sleep(2)

                # Press F8 again to start the macro
                print("Pressing F8 again to start the macro.")
                press_key(win32con.VK_F8)

                # Reset the start time after typing the command and pressing F8
                no_orange_block_start_time = None

    # Check the screen every second
    while time.time() - last_checked < 1:
        if keyboard.is_pressed('F7'):  # Check again if F7 is pressed while waiting
            print("F7 pressed. Exiting script.")
            break
        time.sleep(0.01)
    last_checked = time.time()

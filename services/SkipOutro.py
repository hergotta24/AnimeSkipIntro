import pyautogui
import os
import time
import cv2


save_folder = "screenshots"

def continuously_take_screenshots(template_path, click_x, click_y):
    try:
        while True:
            screenshot_path = take_screenshot(save_folder)
            if find_image(template_path, screenshot_path):
                print("Image recognized! Clicking...")
                os.remove(screenshot_path)
                click_at_coordinates(click_x, click_y)
                print("Clicked!")
                return True
            else:
                os.remove(screenshot_path)
    except KeyboardInterrupt:
        print("\nStopped.")
            
              
        
# Click at specified coordinates
def click_at_coordinates(x, y):
    print(f"Clicking at coordinates: ({x}, {y})")
    click_coordinates(x, y)

def find_image(template_path, screenshot_path):
    template = cv2.imread(template_path, 0)
    screenshot = cv2.imread(screenshot_path, 0)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.6  # Adjust this threshold as needed
    if max_val >= threshold:
        return True  # Image found
    return False

# Move the mouse to specific coordinates and click
def click_coordinates(x, y):
    pyautogui.click(x, y)

# Take a screenshot at the current mouse position and save to a folder
def take_screenshot(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    screenshot = pyautogui.screenshot()
    timestamp = time.strftime("%Y%m%d%H%M%S")
    screenshot_path = os.path.join(folder_path, f"screenshot_{timestamp}.png")
    screenshot.save(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    return screenshot_path
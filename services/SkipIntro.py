import pyautogui
import time

def slide_mouse_and_screenshot(start_x, start_y, end_x, end_y, duration, interval=10):
    # Set the initial position of the mouse
    try:
        time.sleep(8)
        pyautogui.moveTo(start_x, start_y)
        time.sleep(8)
        # Calculate the distance to slide
        distance = end_x - start_x

        # Slide the mouse across the X-axis
        pyautogui.dragTo(end_x, end_y, duration=duration)

        # Take screenshots every 'interval' seconds while sliding
        current_x = start_x
        while current_x < end_x:
        # Define the region above the current mouse position to take a screenshot
            screenshot_region = (current_x + 82, start_y - 30, 40, 18)
        
             # Take a screenshot of the defined region
            screenshot = pyautogui.screenshot(region=screenshot_region)
            screenshot.save(f"screenshot_{current_x}.png")  # Save the screenshot with a filename based on the current x-coordinate
        
            # Wait for 'interval' seconds
            time.sleep(interval)
        
             # Move to the next x-coordinate
            current_x += distance // (duration * 10)  # Move 1/10th of the distance each time (adjust as needed)

    except KeyboardInterrupt:
            print("\nStopped.")

def default_skip_intro(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click(x, y)
    time.sleep(1)
    pyautogui.press('space')
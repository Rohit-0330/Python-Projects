import time
import pyautogui

def auto_screenshot(interval):
    count = 1
    while True:
        filename = f"screenshot_{count}.png"
        image = pyautogui.screenshot()
        image.save(filename)
        print(f"Saved {filename}")
        count += 1
        time.sleep(interval)

if __name__ == "__main__":
    sec = int(input("Screenshot interval (in seconds): "))
    auto_screenshot(sec)

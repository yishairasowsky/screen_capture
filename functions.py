import calendar
import cv2
import numpy as np
import pyautogui
from datetime import datetime

def current_time():
    return str(datetime.now()).split()[1][:5]

def current_weekday():
    return calendar.day_name[datetime.now().weekday()]

def current_date():
    return datetime.now().isoformat()[:10]

def intervals(usage):    
    if usage == 'test':
        low, high = 5, 6
    if usage == 'real':
        max_minutes = 10
        seconds_per_minute = 60
        max_seconds = max_minutes*seconds_per_minute
        low, high = 60, max_seconds
    return low, high

def capture_image(filename):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR) # convert from not sure what this does
    cv2.imwrite(filename, image) # store image in file

if __name__ == "__main__":
    print(current_date())
    pass
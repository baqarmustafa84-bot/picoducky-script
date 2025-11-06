import pyautogui
import time

SHORT_DELAY = 0.75
LONG_DELAY_APP_LAUNCH = 3.0

def launch_and_arrange_workflow():
    pyautogui.FAILSAFE = True

   
    pyautogui.hotkey('command','space')
    time.sleep(SHORT_DELAY)
    pyautogui.write('Spotify')
    time.sleep(SHORT_DELAY)
    pyautogui.press('enter')
    time.sleep(LONG_DELAY_APP_LAUNCH)

    pyautogui.click(pyautogui.size().width / 2, pyautogui.size().height / 2)
    time.sleep(SHORT_DELAY)

    pyautogui.hotkey('command', 'k')
    time.sleep(SHORT_DELAY)
    pyautogui.write('pyari')
    time.sleep(1.0)
    pyautogui.press('enter')
    time.sleep(0.5)
  
    time.sleep(2.0)

    pyautogui.hotkey('command', 'space')
    time.sleep(SHORT_DELAY)
    pyautogui.write('capcut')
    time.sleep(SHORT_DELAY)
    pyautogui.press('enter')
    time.sleep(LONG_DELAY_APP_LAUNCH + 1.0)

   
    pyautogui.hotkey('command', 'space')
    time.sleep(SHORT_DELAY)
    pyautogui.write('http://adobe.com') 
    time.sleep(SHORT_DELAY)
    pyautogui.press('enter')
    time.sleep(LONG_DELAY_APP_LAUNCH)


    browser_window = None 
    capcut_window = None 
    
    for title in ['Google Chrome', 'Safari', 'Firefox']:
        windows = pyautogui.getWindowsWithTitle(title) 
        if windows:
            browser_window = windows[0]
            break
            
    windows = pyautogui.getWindowsWithTitle('CapCut')
    if windows:
        capcut_window = windows[0]

    if browser_window and capcut_window:
        screen_width , screen_height = pyautogui.size() 
        half_width = screen_width // 2

        capcut_window.activate()
        capcut_window.moveTo(0, 0)
        capcut_window.resizeTo(half_width, screen_height)

        time.sleep(SHORT_DELAY)

        browser_window.activate()
        browser_window.moveTo(half_width, 0)
        browser_window.resizeTo(half_width, screen_height)
    else:
        pyautogui.hotkey('command', 'tab')
        time.sleep(SHORT_DELAY)
        pyautogui.hotkey('command', 'tab')


if __name__ == "__main__":
    launch_and_arrange_workflow()
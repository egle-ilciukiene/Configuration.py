import time

from pywinauto import Application, findwindows, Desktop
from pywinauto.timings import wait_until
from appium import webdriver

desktop = Desktop(backend="uia")
nordlocker_app = Application()
nordlocker_app.start('C:\\Program Files\\NordLocker\\NordLauncher.exe', timeout=10)
connected_nordlocker = Application(backend="uia")

try:
    connected_nordlocker.connect(title='NordLocker')
except findwindows.WindowAmbiguousError:
    wins = findwindows.find_elements(active_only=True, title="NordLocker")
    connected_nordlocker.connect(handle=wins[0].handle)
except findwindows.ElementNotFoundError:
    wait_until(30, 0.5, lambda: len(findwindows.find_elements(active_only=True, title="NordLocker")) > 0)
    wins = findwindows.find_elements(active_only=True, title="NordLocker")
    connected_nordlocker.connect(handle=wins[0].handle)

main_screen = connected_nordlocker.window(title='NordLocker')


def timeoutError():
    main_screen = connected_nordlocker.window(title='NordLocker')
    try:
        actionable_window = main_screen.wait("exists enabled visible ready", timeout=20)
    except TimeoutError as e:
        print("Baigesi sesijos laikas")

        print(f"NordLocker app identifier: {main_screen}")


desktop = Desktop(backend="uia")
login_screen = desktop.window(title="NordLocker", control_type="Window")
drop_down = login_screen.child_window(auto_id="HeaderDropDown", control_type="ToolBar")
drop_down.print_control_identifiers()
drop_down.click_input()
login_button = login_screen.child_window(title="Log in", control_type="Button")
login_button.click_input()
time.sleep(5)

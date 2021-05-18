import time
from appium import webdriver

# Open browser and login
desktopCapabilities = {}
desktopCapabilities["app"] = "Root"
web_desktop = webdriver.Remote("http://127.0.0.1:4723", desktopCapabilities)
web_desktop.window_handles
win = web_desktop.find_element_by_class_name('MozillaWindowClass')
win_handle1 = win.get_attribute("NativeWindowHandle")
win_handle = format(int(win_handle1), 'x')
desired_caps = {}
desired_caps["appTopLevelWindow"] = win_handle
driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
driver.switch_to.window(win_handle)
print(driver)

time.sleep(5)

# Login username page
username = driver.find_element_by_name("Username or email address")
username.send_keys("egle.ilciukiene+10@nordsec.com")
driver.find_element_by_name("Continue").click()

time.sleep(5)

# Login password page
userpass = driver.find_element_by_name("Password")
userpass.send_keys("nordlocker1")
show_pass = driver.find_element_by_name("toggle password visibility")
show_pass.click()
driver.find_element_by_name("Log In").click()

# Wait Permissions modal and click Open app button
time.sleep(5)
# permission_button = driver.find_element_by_name("Open Link")
# permission_button.click()
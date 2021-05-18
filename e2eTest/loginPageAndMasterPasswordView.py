import os
import time

# Closed Selenium driver
def close():
    driver.stop_client()
    driver.close()

# Run the driver
pid = os.startfile(r'C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe')
print(f"WinAppDriver pid: {os.getpid()}")

# Open the NordLocker
from RunNordLocker.publicClass.nordLockerLogin import desktop
time.sleep(5)

# Open web browser and login to with Nord Acoount
from RunNordLocker.publicClass.browserAccountLogin import driver

# Handle NordLocker app main screen and enter master password
from  RunNordLocker.publicClass.masterPasswordView import enterMasterPassword

# Open Show Hidden icons block in Systray
from RunNordLocker.publicClass.closeSystrayIcon import systrayIconClose

# Closed opened browser
close()
# Closed WinAppDriver process
from RunNordLocker.publicClass.KillOsProcessByName import KillOsProcessByName as kills_app
kills_apps = kills_app("WinAppDriver.exe")
time.sleep(2)
kills_apps.kill_by_process_name_shell()

# Handle NordLocker app main screen
import time

from pywinauto import Application

from RunNordLocker.publicClass.loginView import desktop
from RunNordLocker.publicClass.nordLockerLogin import nordlocker_app, main_screen


class enterMasterPassword():
        master_screen = desktop.window(title="NordLocker", control_type="Window")
        time.sleep(10)
        master_screen.print_control_identifiers()
        mp_input_field = master_screen.child_window(class_name="PasswordBox", control_type="Edit")
        mp_input_field.select()
        mp_input_field.type_keys("nordlocker1")
        mp_button = master_screen.child_window(title="", control_type="Button")
        mp_button.click_input()

        nordlocker_tray_app = Application(backend="uia").connect(path=r"C:\Program Files\NordLocker\NordLocker.SysTray.exe")

        print()
        print("App name")
        print()
        print([w.window_text() for w in nordlocker_app.windows()])
        print()
        print("------ Print NordLocker control identifiers ------")
        print()
        main_screen.print_control_identifiers()

        print()
        print("----------------------- end ----------------------")
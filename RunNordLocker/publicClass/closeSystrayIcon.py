import time

from RunNordLocker.publicClass.nordLockerLogin import desktop

# Open Show Hidden icons block in Systray
class systrayIconClose():
    systray_block = desktop.window(class_name="Shell_TrayWnd")
    hidden_icons_block = systray_block.child_window(title="Notification Chevron").wrapper_object()
    print(hidden_icons_block)

    time.sleep(5)

    hidden_icons_block.click()

    list_box_win = desktop.window(class_name="NotifyIconOverflowWindow")
    list_box_win.wait('visible', timeout=30, retry_interval=5)

# Logout from app
    quit_tray_app = list_box_win.child_window(title_re="NordLocker*", control_type="Button").wrapper_object()
    print(quit_tray_app)
    quit_tray_app.click_input(button="right")

    time.sleep(2)

    menu_item = desktop.window(class_name="Popup")
    menu_item.print_control_identifiers()
    menu_item.child_window(title="Log Out", control_type="MenuItem").click_input()

# If tray block stay opened need click on tray block icon
# hidden_icons_block.click()

# quit app
    systray_block = desktop.window(class_name="Shell_TrayWnd")
    hidden_icons_block = systray_block.child_window(title="Notification Chevron").wrapper_object()
    print(hidden_icons_block)

    time.sleep(5)

    hidden_icons_block.click()

    list_box_win = desktop.window(class_name="NotifyIconOverflowWindow")
    list_box_win.wait('visible', timeout=30, retry_interval=5)

    quit_tray_app = list_box_win.child_window(title_re="NordLocker*", control_type="Button").wrapper_object()
    print(quit_tray_app)
    quit_tray_app.click_input(button="right")

    time.sleep(2)

    menu_item = desktop.window(class_name="Popup")
    menu_item.print_control_identifiers()
    menu_item.child_window(title="Quit NordLocker", control_type="MenuItem").click_input()

    hidden_icons_block.click()
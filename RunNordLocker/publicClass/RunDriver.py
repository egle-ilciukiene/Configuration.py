import os


class RunDriver:
    def __init__(self, path):
        self.path = path

    def start_winapp_driver(self):
        os.startfile(self.path)
        print(f"WinAppDriver pid: {os.getpid()}")

    def get_app_pid(self):
        return print(f"WinAppDriver pid: {os.getpid()}")

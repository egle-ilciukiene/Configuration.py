import os

class KillOsProcessByName:
    def __init__(self, name):
        self.name = name

    # Killed os process by process name
    def kill_by_process_name_shell(self):
        os.system(f"taskkill /f /im {self.name}")
        # return kill
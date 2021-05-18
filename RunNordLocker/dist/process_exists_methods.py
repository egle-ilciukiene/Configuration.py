import os
import psutil
from subprocess import check_output


def process_exists_best(name):
    # reading the output
    output = os.popen("""wmic process get name | findstr /v "Name 'System Idle Process' System""").read().strip()
    # your items are separated by end of line - so we will split it
    result_items = output.split()
    print(result_items)
    # let's do the search and print the result message
    success = False
    for search in [name]:
    # for search in ['WinAppDriver.exe']:
        if search in result_items:
            success = True
            print(search + " found")
            break
    if not success:
        print("Nothing found")


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    if check_output(call).splitlines()[3:]:
        return print("Process exists")


def process_exists2(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    processes = []
    for process in check_output(call).splitlines()[3:]:
        process = process.decode()
        processes.append(process.split(", "))
    return processes


def process_exists3(name):
    i = psutil.process_iter()
    for proc in i:
        try:
            if proc.name() == name:
                print(proc)
                print(proc.cmdline())
        except psutil.AccessDenied:
            print("Permission error or access denied on process")


# procObjList = [procObj for procObj in psutil.process_iter() if 'winappdriver' in procObj.name().lower() ]
# print(procObjList)
# name = str(procObjList[0])
# new_name = name.split(", ")
#
# new_list = []
# print(new_name)

# for p in psutil.process_iter(attrs=['pid', 'name']):
#     if p.info['name'] == "winappdriver.exe":
#         print("yes", (p.info['name']))


# ================================
# Running the aforementioned command and saving its output
output = os.popen('wmic process get description').read()

# Displaying the output
print(output)
# =================================

# help = os.system(f"tasklist /?")
# run_proc = os.system(f"tasklist /svc /fo list")
image_name = os.system(f'tasklist /fi "imagename eq winappdriver.exe" /fi "Status eq Running" /fo list | findstr /B "Image name:"')



import os

def test_process_exists(name):
    # reading the output
    output = os.popen("""wmic process get name | findstr /v "Name 'System Idle Process' System""").read().strip()
    # your items are separated by end of line - so we will split it
    result_items = output.split()
    # let's do the search and print the result message
    success = False
    for search in [name]:
    # for search in ['WinAppDriver.exe']:
        if search in result_items:
            success = True
            assert search == "WinAppDriver.exe"
            # print(search + " found")
            break
    if not success:
        print("Nothing found")
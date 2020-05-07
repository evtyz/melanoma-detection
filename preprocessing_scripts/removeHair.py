# Run order: 5
# Preprocess images by removing hairs from each one using DullRazor

from pywinauto.keyboard import send_keys
from pywinauto.application import Application
from pywinauto.timings import TimeoutError
import subprocess
import pathlib
import sys

sys.setrecursionlimit(20000)

DULLRAZOR_DIRECTORY_ROOT = "D:/Internet Downloads"
DULLRAZOR_ROOT = DULLRAZOR_DIRECTORY_ROOT + "/dullrazor_wins/dullrazor.exe"

PATH = "D:/isic-image-database/"

pathlist = list(pathlib.Path(PATH).glob("*/*/*.jpg"))
total = len(pathlist)

def runApp(index):

    global DULLRAZOR_ROOT, pathlist, total

    app = Application().start(DULLRAZOR_ROOT)
    window = app.window(title='DullRazor for Windows')
    window2 = app.window(title='dullrazor')

    # Every 80-85 runs, Dullrazor crashes for an unknown reason, so we have to restart it.
    try:
        currentIndex = index
        while currentIndex < total:
            print(currentIndex)
            path = pathlist[currentIndex]
            subprocess.run(['clip.exe'], input=str(path).strip().encode('utf-8'), check=True)
            send_keys("{TAB}{TAB}{TAB}{TAB}{TAB}^v{TAB}{TAB}^v{TAB}{TAB}{TAB}{ENTER}")
            window2.wait('exists', timeout=20)
            send_keys("{ENTER}")
            currentIndex += 1
    except TimeoutError:
        runApp(currentIndex)

runApp(0)

# Tab-order goes:
# 1. Exit
# 2. Produce Hairmask
# 3. Produce Extended Hairmask
# 4. Post-Op Smoothing
# 5. Select source file to process
# 6. Source file browse
# 7. Select target file to process
# 8. Target file browse
# 9. Clear
# 10. Start

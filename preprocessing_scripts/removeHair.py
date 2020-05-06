# Run order: 5
# Preprocess images by removing hairs from each one using DullRazor

from pywinauto.keyboard import send_keys
from pywinauto.application import Application
import subprocess
import pathlib
import time

DULLRAZOR_DIRECTORY_ROOT = "D:/Internet Downloads"
DULLRAZOR_ROOT = DULLRAZOR_DIRECTORY_ROOT + "/dullrazor_wins/dullrazor.exe"

ROOT = "D:/Internet Downloads/"
PATH = ROOT + "ISIC-images/"

app = Application().start(DULLRAZOR_ROOT)
window = app.window(title='DullRazor for Windows')

pathlist = pathlib.Path(PATH).glob("*/*/*.jpg")

# pathlist = pathlib.Path("D:/Internet Downloads/dullrazortrial/").glob("*.jpg")

counter = 0
for path in pathlist:
    counter += 1
    print(counter)
    subprocess.run(['clip.exe'], input=str(path).strip().encode('utf-8'), check=True)
    send_keys("{TAB}{TAB}{TAB}{TAB}{TAB}^v{TAB}{TAB}^v{TAB}{TAB}{TAB}{ENTER}")
    window.wait_not('active')
    send_keys("{ENTER}")

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

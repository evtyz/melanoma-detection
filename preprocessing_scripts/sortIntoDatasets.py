# Run order: 3

# Distribute benign and malignant images to training, validation, test sets

# Training: 80%
# Validation: 10%
# Test: 10%

import pathlib
import shutil
import os

ROOT = "D:/Internet Downloads/ISIC-images/"
BENIGN_PATH = ROOT + "benignPlaceholder/"
MALIGNANT_PATH = ROOT + "malignantPlaceholder/"
TRAINING_PATH = ROOT + "training/"
VALIDATION_PATH = ROOT + "validation/"
TEST_PATH = ROOT + "test/"

ROOT_PATHS = [TRAINING_PATH, VALIDATION_PATH, TEST_PATH]
CLASSES = ["benign/", "malignant/"]

for root in ROOT_PATHS:
    os.mkdir(root)
    for classification in CLASSES:
        os.mkdir(root+classification)


benignPathList = pathlib.Path(BENIGN_PATH).glob("*.jpg")
malignantPathList = pathlib.Path(MALIGNANT_PATH).glob("*.jpg")

def distribute(pathList, classification):
    global VALIDATION_PATH, TEST_PATH, TRAINING_PATH

    counter = 0
    for path in pathList:
        name = path.name
        copyPath = str(path)
        counter += 1
        key = counter % 10
        if key == 1:
            pastePath = VALIDATION_PATH + classification + name
        elif key == 2:
            pastePath = TEST_PATH + classification + name
        else:
            pastePath = TRAINING_PATH + classification + name
        
        shutil.move(copyPath, pastePath)

distribute(benignPathList, "benign/")
distribute(malignantPathList, "malignant/")

os.rmdir(BENIGN_PATH)
os.rmdir(MALIGNANT_PATH)
# Run order: 2

# Sorts images into benign and malignant categories based on a ground-truth CSV file

import csv
import pathlib
import shutil
import os

ROOT = "D:/Internet Downloads/ISIC-images/"
METADATA_PATH = ROOT + "metadata.csv"

with open(METADATA_PATH, mode='r') as infile:
    reader = csv.DictReader(infile)
    groundTruths = {row['name'] : row['meta.clinical.benign_malignant'] for row in reader} 

print(groundTruths)

BENIGN_PATH = ROOT + "benignPlaceholder/"
MALIGNANT_PATH = ROOT + "malignantPlaceholder/"

os.mkdir(BENIGN_PATH)
os.mkdir(MALIGNANT_PATH)

pathList = pathlib.Path(ROOT).glob("*/*.jpg")
for path in pathList:
    fileName = path.name
    key = groundTruths[path.name.strip(".jpg")]
    if key == "benign":
        pastePath = BENIGN_PATH + path.name
    elif key == "malignant":
        pastePath = MALIGNANT_PATH + path.name
    else:
        print("error")
        continue
    copyPath = str(path)
    shutil.move(copyPath, pastePath)





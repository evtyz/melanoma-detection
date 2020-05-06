# Run order: 6
# Optimize the size of each image

from PIL import Image
import pathlib

def Optimize_Image(ImageFilePath):
    image = Image.open(ImageFilePath)
    image.save(ImageFilePath, optimize=True)

ROOT = "D:/Internet Downloads/ISIC-images/"

pathList = pathlib.Path(ROOT).glob("*/*/*.jpg")

# pathList = pathlib.Path("D:/Internet Downloads/dullrazortrial/").glob("*.jpg")

counter = 0
for path in pathList:
    counter += 1
    Optimize_Image(path)
    print(counter)
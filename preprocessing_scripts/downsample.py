# Run order: 4

# Downsample images to at-most 896x896

from PIL import Image
import pathlib

def Downsize_Image(ImageFilePath):
    image = Image.open(ImageFilePath, 'r')
    image_size = image.size[0]
    
    DOWNSAMPLE_SIZE = 224

    if image_size > DOWNSAMPLE_SIZE:
        image = image.resize((DOWNSAMPLE_SIZE, DOWNSAMPLE_SIZE), resample=Image.LANCZOS)
        image.save(ImageFilePath)
        print("Image downsampled!")
    else:
        print("Image already downsampled enough!")

ROOT = "D:/isic-image-database/"

pathList = pathlib.Path(ROOT).glob("*/*/*.jpg")

counter = 0
for path in pathList:
    counter += 1
    Downsize_Image(path)
    print(counter)


    
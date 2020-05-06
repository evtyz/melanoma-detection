from PIL import Image
import pathlib

def Reformat_Image(ImageFilePath):
    image = Image.open(ImageFilePath, 'r')
    image_size = image.size
    width = image_size[0]
    height = image_size[1]

    if width != height:
        smallside = width if width < height else height

        left = (width-smallside) // 2
        top = (height-smallside) // 2
        right = left + smallside
        bottom = top + smallside

        assert right-left == bottom-top
        image = image.crop((left, top, right, bottom))
        image.save(ImageFilePath)
        print("Image resized!")
    else:
        print("Image already resized!")

ROOT = "D:/Internet Downloads/ISIC-images/"

pathList = pathlib.Path(ROOT).glob("*/*.jpg")

counter = 0
for path in pathList:
    counter += 1
    Reformat_Image(path)
    print(counter)

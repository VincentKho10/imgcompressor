from PIL import Image
import os, sys

def processImage(file_path):
    decper = int(input("Input quality (max 100 & min 1):"))
    if(decper<=100 and decper>0):
        with Image.open(file_path, 'r') as img:
            # width,height = img.size
            # new_size = (int(width*decper),int(height*decper))
            # resize = img.resize(new_size)
            img.save('compressed/compressed.jpg', optimize=True, quality=decper)
    else:
        print('percentage is on max or exceed limit')
        return


if __name__ == '__main__':
    file_path = sys.argv
    if len(file_path) < 2:
        print('Please provide file as an argument.')
    else:
        processImage(file_path[1])
    input('press any key...')
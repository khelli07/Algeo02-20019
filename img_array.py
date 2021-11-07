from PIL import Image
import numpy as np

def load_image():
    img_name = input("Input image name: ")
    image = Image.open(img_name)

    img_arr = np.asfarray(image)
    print(img_arr)
    print(img_arr.shape)

    return img_arr

# load_image()
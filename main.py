import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import bener as Operator
from PIL import Image
from datetime import datetime, date

# from img_array import load_image

def blackAndWhite():
    # load_image()
    img = cv.imread('./lena.png')
    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    img_array = np.asarray(img)

    # Show image
    plt.imshow(img, cmap='gray')
    plt.show()

    #Pecah matrix
    rank = int(img_array.shape[0] / 1)
    #Belum efisien
    # uImage,sImage,vImage = Operator.methodSVD(img_array)

    # ini 6 menit buat 512x512 (100%)
    uImage,sImage,vImage = Operator.svd(img_array,rank)

    # # ini numpy
    #uImage,sImage,vImage = np.linalg.svd(img_array)
    compresedImg = Operator.constructNewImg(uImage,sImage,vImage,rank)
    print(compresedImg.shape)
    #
    plt.imshow(compresedImg, cmap='gray')
    plt.show()

def color():
    img = cv.imread('./lena.png')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_array = np.asarray(img)
    imageRed,imageGreen,imageBlue = rgbMatrix(img_array)

    # Show image
    plt.imshow(img)
    plt.show()

    # 
    uRed,sRed,vRed = Operator.methodSVD(imageRed)
    uGreen,sGreen,vGreen = Operator.methodSVD(imageGreen)
    uBlue,sBlue,vBlue = Operator.methodSVD(imageBlue)

    rank = int(img_array.shape[0] / 20)
    compresedRed = Operator.constructNewImg(uRed,sRed,vRed,rank) 
    compresedGreen = Operator.constructNewImg(uRed,sGreen,vGreen,rank) 
    compresedBlue =Operator.constructNewImg(uBlue,sBlue,vBlue,rank) 

    imr = Image.fromarray(compresedRed, mode=None)
    img = Image.fromarray(compresedGreen, mode=None)
    imb = Image.fromarray(compresedBlue, mode=None)
    compresedImg = Image.merge("RGB", (imr, img, imb))

def rgbMatrix(matrix):

    aRed = matrix[:, :, 0]
    aGreen = matrix[:, :, 1]
    aBlue = matrix[:, :, 2]

    return [aRed, aGreen, aBlue]

start = datetime.now().time()
print(start)
blackAndWhite()
end = datetime.now().time()
duration = datetime.combine(date.min, end) - datetime.combine(date.min, start)
print(duration)
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import bener as Operator
from PIL import Image
from datetime import datetime, date

print(datetime.now().time())

# img = cv.imread('./tester/guild.png')
img = cv.imread('./lena.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

img_array = np.asarray(img)
print(img_array.shape)
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(img)
plt.show()
print(img_array)
def rgbMatrix(matrix):

    aRed = matrix[:, :, 0]
    aGreen = matrix[:, :, 1]
    aBlue = matrix[:, :, 2]

    return [aRed, aGreen, aBlue]

# imageRed,imageGreen,imageBlue = rgbMatrix(img_array)
start = datetime.now().time()



# uRed,sRed,vRed = Operator.methodSVD(imageRed)
# print(datetime.datetime.now().time())
# uGreen,sGreen,vGreen = Operator.methodSVD(imageGreen)
# print(datetime.datetime.now().time())
# uBlue,sBlue,vBlue = Operator.methodSVD(imageBlue)
# print(datetime.datetime.now().time())
uImage,sImage,vImage = Operator.methodSVD(img_array)

# uRed,sRed,vRed = np.linalg.svd(imageRed)
# print(datetime.now().time())
# uGreen,sGreen,vGreen = np.linalg.svd(imageGreen)
# print(datetime.now().time())
# uBlue,sBlue,vBlue = np.linalg.svd(imageBlue)
# print(datetime.now().time())
x = int(img_array.shape[0] / 20)
# uImage,sImage,vImage = np.linalg.svd(img_array)

# uImage,sImage,vImage = Operator.svd(img_array,x)
# uRed,sRed,vRed = Operator.svd(imageRed,x)
# print(datetime.now().time())
# uGreen,sGreen,vGreen = Operator.svd(imageGreen,x)
# print(datetime.now().time())
# uBlue,sBlue,vBlue = Operator.svd(imageBlue,x)
# print(datetime.now().time())



#uImageLin,sImageLin,vImageLin = np.linalg.svd(img_array)
# print(sImage)
# print("tes")
# print(sImageLin)

# print(vImage)
# print(vImageLin)


# print(uImage.shape)
# print(sImage.shape)
# print(vImage.shape)

# compresedRed = Operator.constructNewImg(uRed,x) @ Operator.constructNewImg(sRed,x) @Operator.constructNewImg(vRed,x)
# compresedGreen = Operator.constructNewImg(uGreen,x) @ Operator.constructNewImg(sGreen,x) @Operator.constructNewImg(vGreen,x)
# compresedBlue =Operator.constructNewImg(uBlue,x) @ Operator.constructNewImg(sBlue,x) @Operator.constructNewImg(vBlue,x)


# compresedRed = Operator.constructNewImg(uRed,sRed,vRed,x) 
# compresedGreen = Operator.constructNewImg(uRed,sGreen,vGreen,x) 
# compresedBlue =Operator.constructNewImg(uBlue,sBlue,vBlue,x) 
compresedImg = Operator.constructNewImg(uImage,sImage,vImage,x)
# compresedImg = Operator.constructNewImg(uImageLin,sImageLin,vImageLin,x)


# matrix = np.asarray(gray_img)
# matrix

# sigma = np.array([[0.0 for i in range(x)] for j in range(x)])
# for i in range(x):
#     sigma[i][i] = np.sqrt(sImage)[i]


# compresedImg = uImage @ sigma@ vImage

# imr = Image.fromarray(compresedRed, mode=None)

# img = Image.fromarray(compresedGreen, mode=None)
# imb = Image.fromarray(compresedBlue, mode=None)



# compresedImg = Image.merge("RGB", (imr, img, imb))
img_array = np.asarray(compresedImg)
print(img_array.shape)
plt.imshow(compresedImg, cmap='gray')
plt.show()
end = datetime.now().time()

duration = datetime.combine(date.min, end) - datetime.combine(date.min, start)
print(duration)
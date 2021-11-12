#####################################################
#   The code was made to complete                   #
#   IF2123 Linear Algebra and Geometry Course       #
#   Bandung Institute of Technology                 #
#                                                   #
#   Made with <3 by:                                #
#   - Maria Khelli                                  #
#   - Maharani Ayu Putri Irawan                     #
#   - Suryanto                                      #
#####################################################
'''
Source: 
Handbook for Automatic Computation Linear Algebra (p. 241-248)
The Implicit QL Algorithm
by Reinsch, Martin, and Wilkinson 
'''
#   IMPORTS
from scipy import linalg
import numpy as np
import cv2 as cv
import math
from PIL import Image

#   CODES
def sign(number):
    return 1 if (round(number, 3) > 0) else -1
    
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def isFlipped(matrix):
    row, col = matrix.shape
    return (row < col)
def getEigenRight(mat, eps = 1.e-5):
    mat = np.matrix(mat, dtype=np.float64)
    smat = np.matmul(mat.T, mat)

    # Params
    hess, singularMatrix = linalg.hessenberg(smat, calc_q=True)
    diag = [np.float64(val) for val in np.diag(hess)]
    subdElmt = [np.float64(val) for val in np.diag(hess, -1)]

    # Start
    n = len(diag)
    itermax = 1//eps**2
    subdElmt.append(0)

    for l in range(n):
        j = 0
        while True:
            m = l
            while True:
                
                if (m + 1) == n:
                    break
                
                if abs(subdElmt[m]) <= eps * (abs(diag[m]) + abs(diag[m + 1])):
                    break 
                m += 1
            
            if m == l:
                break 
            
            if j >= itermax:
                raise RuntimeError(f"No convergence to eigenvalue after {j} iteration.")

            j += 1

           
            p = diag[l]
            g = (diag[l + 1] - p) / (2 * subdElmt[l])
            r = hypotenuse(g, 1)

          
            sin = g + sign(g)*r

            g = diag[m] - p + subdElmt[l] / sin

            sin, cos, p = 1, 1, 0

            for i in range(m - 1, l - 1, -1):
                f = sin * subdElmt[i]
                b = cos * subdElmt[i]
                if abs(f) > abs(g):
                    cos = g / f 
                    r = hypotenuse(cos, 1)
                    subdElmt[i + 1] = f * r 
                    sin = 1 / r
                    cos *= sin
                else:
                    sin = f / g if g != 0 else 0
                    r = hypotenuse(sin, 1)
                    subdElmt[i + 1] = g * r 
                    cos = 1 / r 
                    sin *= cos 
                
                g = diag[i + 1] - p 
                r = (diag[i] - g) * sin + 2 * cos * b 
                p = sin * r 
                diag[i + 1] = g + p 
                g = cos * r - b 

                
                singularMatrix[:, i:i + 2] = singularMatrix[:, i:i + 2]\
                                            .dot(np.array([[cos, sin],
                                                          [-sin, cos]], dtype=np.float64))
 
            diag[l] -= p
            subdElmt[l] = g
            subdElmt[m] = 0

    eigenval = np.array(diag.copy())
    eigenval[np.where(eigenval < 0)] = 0
    sortedIdx = np.argsort(eigenval)[::-1]
    singularMatrix = singularMatrix[:, sortedIdx]
    eigenval = np.sort(eigenval)[::-1]

    return eigenval, singularMatrix

def getSVD(matrix):
    matrix = np.matrix(matrix, dtype=np.float64)
    mcopy = matrix.copy()
    row, col = mcopy.shape

   
    if isFlipped(matrix):
        mcopy = mcopy.T
        row, col = mcopy.shape

    u = np.zeros((row, row))
    eigval, v = getEigenRight(mcopy)

   
    sigma = np.array([math.sqrt(x) for x in eigval if x != 0])
    maxrank = len(sigma)
    
    
    for i in range(maxrank):
        u[:, i] = mcopy @ v[:, i] / sigma[i]

    return u, sigma, v, maxrank

def getReducedMatrix(matrix, percent):
    matrix = np.matrix(matrix, dtype=np.float64)
    row, col = matrix.shape
    
    u, sigma, v, maxrank = getSVD(matrix)
    percent = 100 - percent
    r = math.ceil(percent/100 * maxrank)

    matsig = np.matrix(np.zeros((row, col)), dtype=np.float64)
    np.fill_diagonal(matsig, sigma)
    ui = np.matrix(u[:, :r])
    vi = np.matrix(v.T[:r, :])
    reduced = ui @ matsig[:r, :r] @ vi

    if isFlipped(matrix):
        return reduced.T
    else:
        return reduced

def compressImage(imagepath, percent, outputName):
    img = Image.open(imagepath)
    format = imagepath.split(".")

    
    # print(img.shape)
    channel = img.getbands()
    print(channel)
    # Handle file such as .png
    if (channel[0] == "L"  and len(channel)==1):
        img =  np.asarray(img)
        gray = img.copy()
        reducedPict = getReducedMatrix(gray, percent)
        # cv.imwrite(outputName, img)
        result= Image.fromarray(np.uint8(reducedPict))
        result.save(outputName)

    # PNG yang berwarna dan memiliki alpha channel
    elif (channel[0] == "P"  and len(channel)==1) or (channel ==('R','G','B','A')) :
        img = img.convert("RGBA")
        img =  np.asarray(img)

        r = img[:,:,0]
        g = img[:,:,1]
        b = img[:,:,2]

        # b, g, r, a = cv.split(img)
        reducedRed = getReducedMatrix(r, percent)
        reducedGreen = getReducedMatrix(g, percent)
        reducedBlue = getReducedMatrix(b, percent)

        img[:,:,0] = reducedRed
        img[:,:,1] = reducedGreen
        img[:,:,2] = reducedBlue
        img = np.clip(img,0,255)

        result = Image.fromarray(np.uint8(img)).convert("P")
        result.save(outputName)

    #PNG warna tanpa alpha atau JPG 
    elif (channel == ('R','G','B')):


        if (format[1]=='png'):
            numberOfChannel = np.asarray(img).shape[2]
            if (numberOfChannel != 3):
                img = img.convert("RGBA")

        img =  np.asarray(img)

        r = img[:,:,0]
        g = img[:,:,1]
        b = img[:,:,2]

        # b, g, r, a = cv.split(img)
        reducedRed = getReducedMatrix(r, percent)
        reducedGreen = getReducedMatrix(g, percent)
        reducedBlue = getReducedMatrix(b, percent)

        img[:,:,0] = reducedRed
        img[:,:,1] = reducedGreen
        img[:,:,2] = reducedBlue
        img = np.clip(img,0,255)

        result = Image.fromarray(np.uint8(img))
        if (format[1]=='png'):
            result.convert("P")

        result.save(outputName)

    # else:
        # if (format[1]=='png'):
        #     numberOfChannel = np.asarray(img).shape[2]
        #     if (numberOfChannel != 3):
        #         img = img.convert("RGBA")

        # img =  np.asarray(img)

        # r = img[:,:,0]
        # g = img[:,:,1]
        # b = img[:,:,2]

        # # b, g, r, a = cv.split(img)
        # reducedRed = getReducedMatrix(r, percent)
        # reducedGreen = getReducedMatrix(g, percent)
        # reducedBlue = getReducedMatrix(b, percent)

        # img[:,:,0] = reducedRed
        # img[:,:,1] = reducedGreen
        # img[:,:,2] = reducedBlue
        # img = np.clip(img,0,255)

        # result = Image.fromarray(np.uint8(img))
        # # if (format[1]=='png'):
        # #     result.convert("P")

        # result.save(outputName)

    return result
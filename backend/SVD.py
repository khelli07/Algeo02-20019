#####################################################
#   The code was made to complete                   #
#   IF2123 Linear Algebra and Geometry Course       #
#   Bandung Institute of Technology                 #
#                                                   #
#   Made with <3 by:                                #
#   - Maria Khelli                                  #
#   - Maharani Ayu Putri Irawan                     #
#   - Suryanto Tan                                  #
#####################################################
'''
Source: 
Handbook for Automatic Computation Linear Algebra (p. 241-248)
The Implicit QL Algorithm
by Reinsch, Martin, and Wilkinson 
'''
#   IMPORTS
import matplotlib.pyplot as plt
from scipy import linalg
import numpy as np
import cv2 as cv
import math

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
                # Convergence test
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

            # Form shift
            p = diag[l]
            g = (diag[l + 1] - p) / (2 * subdElmt[l])
            r = hypotenuse(g, 1)

            # Avoiding cancelation
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
                    sin = f / g 
                    r = hypotenuse(sin, 1)
                    subdElmt[i + 1] = g * r 
                    cos = 1 / r 
                    sin *= cos 
                
                g = diag[i + 1] - p 
                r = (diag[i] - g) * sin + 2 * cos * b 
                p = sin * r 
                diag[i + 1] = g + p 
                g = cos * r - b 

                # Compute eigenvectors
                singularMatrix[:, i:i + 2] = singularMatrix[:, i:i + 2]\
                                            .dot(np.array([[cos, sin],
                                                          [-sin, cos]], dtype=np.float64))
 
            diag[l] -= p; subdElmt[l] = g; subdElmt[m] = 0

    eigenval = np.array(diag.copy())
    eigenval[np.where(eigenval < 0)] = 0
    sortedIdx = np.argsort(eigenval)[::-1]
    singularMatrix = singularMatrix[:, sortedIdx]
    eigenval = np.sort(eigenval)[::-1]

    return eigenval, singularMatrix

def getSVD(matrix):
    mcopy = matrix.copy()
    row, col = mcopy.shape

    # Column should be higher than row
    if isFlipped(matrix):
        mcopy = mcopy.T
        row, col = mcopy.shape

    u = np.zeros((row, row))
    eigval, v = getEigenRight(mcopy)

    sigma = [math.sqrt(x) for x in eigval]

    # Compute u from v
    for i in range(col):
        u[:, i] = (mcopy @ v[:, i]) / sigma[i]

    return u, sigma, v

def getReducedMatrix(matrix, percent):
    row, col = matrix.shape
    u, sigma, v = getSVD(matrix)

    maxrank = len([1 for s in sigma if s != 0.0])
    r = int((100 - percent) * maxrank * 1.e-2)

    matsig = np.matrix(np.zeros((row, col)), dtype=np.float64)
    np.fill_diagonal(matsig, sigma)
    ui = np.matrix(u[:, :r])
    vi = np.matrix(v.T[:r, :])
    reduced = ui @ matsig[:r, :r] @ vi

    if isFlipped(matrix):
        return reduced.T
    else:
        return reduced
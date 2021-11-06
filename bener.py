import numpy as np
from numpy.linalg import norm
from scipy.linalg import hessenberg
from random import normalvariate
from math import sqrt


# TODO : IMPLEMENTASI QR manual

# EigenVector + EigenVal
def eigenQR(A):
    temp,_ = hessenberg(A, True)
    #temp = np.copy(A)
    row = temp.shape[0]
    QQ = np.eye(row)

    for i in range(100000):
        c = temp[row-1, row-1]
        cI = c * np.eye(row)
        Q, R = np.linalg.qr(np.subtract(temp, cI))
        temp = np.add(R @ Q, cI)

        QQ = QQ @ Q
    
    return np.diag(temp), QQ

def methodSVD(matrix):
    row, col = matrix.shape
    
    eigAtA, rightSingular= eigenQR(np.transpose(matrix) @ matrix)
    Vt = np.transpose(rightSingular)
    rank = np.count_nonzero(eigAtA)

    #Sigma = np.zeros((row, col))
    SigmaInv = np.zeros((row, col))
    eigSort = np.sort(eigAtA)[::-1]
    #eigAtA = eigAtA[::-1].sort()
    for i in range(len(eigSort)):
        #Sigma[i][i]= np.sqrt(eigSort[i])
        SigmaInv[i][i] = 1/np.sqrt(eigSort[i])

    U = matrix @ Vt @ SigmaInv
    
    return U, eigSort, Vt

def constructNewImg(u,s,v,rank = 10):
    leftSide = np.matmul(u[:, 0:rank], np.diag(s)[0:rank, 0:rank])
    # leftSide = np.matmul(u[:, 0:rank], s[0:rank, :])
  
    matrixSVD = np.matmul(leftSide, v[0:rank, :])
    
    matrixSVDRounded = matrixSVD.astype('uint8')
    
    return matrixSVDRounded
def main():
    m = int(input("nilai m: "))
    n = int(input("nilai n: "))
    matriks = np.array([[0 for i in range(n)] for j in range(m)])
    # matriks = np.array([[0 for i in range(n)] for j in range(m)])


    for i in range(m):
        for j in range(n):
            matriks[i][j] = float(input(("Nilai: ")))

    u,s,v = methodSVD(matriks)
    a,b,c = np.linalg.svd(matriks)



    print(matriks)
    print("======")
    print(u)
    print("======")
    print(s)
    print("======")
    print(v)
    print("======")
    print(s.shape)
    print("======")
    print(a)
    print("======")
    print(b)
    print("======")
    print(c)
    print("======")
    compresedImage = constructNewImg(u,s,v, s.shape[0])
    compresedImagea = constructNewImg(a,b,c, b.shape[0])
    print("===aaa===")
    print(compresedImage)
    print("==xghaa====")
    print(compresedImagea)


def randomUnitVector(n):
    unnormalized = [normalvariate(0, 1) for _ in range(n)]
    theNorm = sqrt(sum(x * x for x in unnormalized))
    return [x / theNorm for x in unnormalized]


def svd_1d(A, epsilon=1e-10):
    ''' The one-dimensional SVD '''

    n, m = A.shape
    x = randomUnitVector(min(n,m))
    lastV = None
    currentV = x

    if n > m:
        B = np.dot(A.T, A)
    else:
        B = np.dot(A, A.T)

    iterations = 0
    while True:
        iterations += 1
        lastV = currentV
        currentV = np.dot(B, lastV)
        currentV = currentV / norm(currentV)

        if abs(np.dot(currentV, lastV)) > 1 - epsilon:
            print("converged in {} iterations!".format(iterations))
            return currentV


def svd(A, k=None, epsilon=1e-3):
    '''
        Compute the singular value decomposition of a matrix A
        using the power method. A is the input matrix, and k
        is the number of singular values you wish to compute.
        If k is None, this computes the full-rank decomposition.
    '''
    A = np.array(A, dtype=float)
    n, m = A.shape
    svdSoFar = []
    if k is None:
        k = min(n, m)

    for i in range(k):
        matrixFor1D = A.copy()
        print(i+1)
        for singularValue, u, v in svdSoFar[:i]:
            matrixFor1D -= singularValue * np.outer(u, v)

        if n > m:
            v = svd_1d(matrixFor1D, epsilon=epsilon)  # next singular vector
            u_unnormalized = np.dot(A, v)
            sigma = norm(u_unnormalized)  # next singular value
            u = u_unnormalized / sigma
        else:
            u = svd_1d(matrixFor1D, epsilon=epsilon)  # next singular vector
            v_unnormalized = np.dot(A.T, u)
            sigma = norm(v_unnormalized)  # next singular value
            v = v_unnormalized / sigma

        svdSoFar.append((sigma, u, v))

    singularValues, us, vs = [np.array(x) for x in zip(*svdSoFar)]
    return us.T,singularValues, vs

def fixEigenVector(matrix):
    m,n = matrix.shape

    for i in range (m):
        if (matrix[0][i]) < 0:
            matrix[:,i] *= -1

    
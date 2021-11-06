import numpy as np
from numpy.core.arrayprint import dtype_is_implied

def mat_norm (mat):
    norm = float(np.max(np.sum(np.abs(mat), axis=0)))
    return norm

def eigenValue (A, x):
    y = A @ x / x
    return float(y[0])

def eigenVector (A, accuracy):
    eiVectorOld = np.ones(A.shape[1]).astype(float)
    evOld = eigenValue(A, eiVectorOld)
    cont = True
    first = True
    while (cont):
        if(not(first)):
            eiVectorOld = eiVectorNew
            evOld = evNew
        x = np.dot(A, eiVectorOld).astype(float)
        norm = mat_norm(x)
        eiVectorNew = (x/norm).astype(float)
        evNew = eigenValue(A, eiVectorNew)
        first = False
        if(float(np.abs(evOld - evNew)) < accuracy):
            cont = False
            return evNew, eiVectorNew

a = np.array([[3, 0], [8, -1]]).astype(float)

eiVector, eiVal = eigenVector(a, 50)

print(eiVector)
print(eiVal)
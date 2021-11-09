import numpy as np
import spl_solution

def factorizationMatrix(a):
    aT = np.transpose(a)
    aAst = np.matmul(aT, a)

    return aAst.astype(float)

def maxEigenValue (aAsterisk):
    i = 0
    eps = 10e-2
    
    eiNew = 0
    eiOld = eiNew
    
    R = np.ones(aAsterisk.shape[0])
    
    delta = eps+1 # dibuat lebih besar daripada eps supaya masuk while
    while (delta > eps):
        V = np.dot(aAsterisk, R)
        print("---- INI V ----")
        print(V)

        if (i == 0):
            M = np.zeros((aAsterisk.shape[0], 1))
            M[:, 0] = np.array(V)
        else:
            M = np.column_stack((M, np.array(V)))
        print(" MMMMMMM ")
        print(M)
        R = V
        if(i > 0):
            eiOld = eiNew
            eiNew = M[1, i]/M[1, i-1]
            delta = abs(eiNew - eiOld)

        i += 1

    return eiNew

def eigenVector(aAsterisk, eigenVal):
    rank = min(aAsterisk.shape[0], aAsterisk.shape[1])
    print("sebelum sebelum")
    print(eigenVal)
    print(aAsterisk)
    for i in range(rank):
        aAsterisk[i, i] -= eigenVal
    print("sebelum")
    print(aAsterisk)
    aAsterisk = np.column_stack((aAsterisk, np.array(np.zeros(aAsterisk.shape[0]))))
    print("sesudah")
    print(aAsterisk)
    col = aAsterisk.shape[1]
    res = ["" for i in range(col-1)]
    num = np.zeros(col-1)
    res, num = spl_solution.GaussJordan(aAsterisk)
    if(res[0] == "No solution (inconsistent)"):
        print("No solution (inconsistent)")
        return np.zeros(len(num))
    else:
        return num

def hermitianMatrix (eiVector):
    num_el = len(eiVector)
    h = np.zeros((num_el, num_el))
    h = spl_solution.IdentityMatrix(num_el)
    for i in range(num_el):
        if(i == 0):
            h[i, 0] /= eiVector[0]
        else:
            h[i, 0] = (-1)*eiVector[i-1]/eiVector[0]
    return h

def inverseHermitianMatrix (eiVector):
    num_el = len(eiVector)
    h = np.zeros((num_el, num_el))
    h = spl_solution.IdentityMatrix(num_el)
    for i in range(num_el):
        if(i == 0):
            h[i, 0] = eiVector[0]
        else:
            h[i, 0] = (-1)*eiVector[i-1]
    return h

def equivalentMatrix (a, eiVector):
    hermitian = hermitianMatrix(eiVector)
    invHermitian = inverseHermitianMatrix(eiVector)
    eq = hermitian @ a @ invHermitian
    ret = np.zeros((eq.shape[0]-1, eq.shape[1]-1))
    for i in range (1, eq.shape[0]):
        for j in range (1, eq.shape[1]):
            ret[i-1, j-1] = eq[i, j]
    return ret

def eigenValuesVectors (a):
    eiVals = []
    aAsterisk = factorizationMatrix(a)
    while (np.count_nonzero(aAsterisk) > 1):
        maxEiVal = maxEigenValue(aAsterisk)
        eiVals.append(maxEiVal)
        eiVector = np.zeros(aAsterisk.shape[0])
        eiVector = eigenVector(aAsterisk, maxEiVal)
        print("eiVector")
        print(eiVector)
        b = np.zeros((aAsterisk.shape[0]-1, aAsterisk.shape[1]-1))
        b = equivalentMatrix(aAsterisk, eiVector)
        aAsterisk = b
    nEiVal = len(eiVals)
    eiVals = np.array(eiVals)
    for i in range(nEiVal):
        eiVector = eigenVector(aAsterisk, eiVals[i])
        if (i == 0):
            eiVectors = np.empty((aAsterisk.shape[i], 1))
            eiVectors[:, 0] = np.array(eiVector)
        else:
            eiVectors = np.column_stack((eiVectors, np.array(eiVector)))
    return eiVals, eiVectors

a = np.array([[3, 1, 0], [1, 2, 2], [0,1,1]]).astype(float)

evl, evs = eigenValuesVectors(a)
print(evl)
print(evs)
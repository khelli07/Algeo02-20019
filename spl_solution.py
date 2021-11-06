import numpy as np
import math

from numpy.core.defchararray import chararray

def countNonZeroRow(start, end, mat):
    cnt = 0
    row = mat.shape[0]
    for i in range(row):
        j = start
        nonZero = False
        while (j <= end and not(nonZero)):
            if(mat[i, j] != 0):
                nonZero = True
            else:
                j += 1
        if(nonZero):
            cnt += 1
    return cnt

def getColLeadingNum(mat, row):
    i = 0
    col = mat.shape[1]

    while (i < col and mat[row, i] == 0):
        i += 1
    if(mat[row, i] != 0):
        return i
    else:
        return -1

def Ref(mat):
    i = 0
    n = 0
    row, col = mat.shape

    while (i < row and n < col):
        maxVal = mat[i, n]
        maxRow = i

        allZero = (maxVal == 0)
        if(allZero):
            j = i + 1
            while (maxVal == 0 and j < row):
                if(mat[j, n] != 0):
                    maxVal = mat[j, n]
                    maxRow = j
                    allZero = False
                j += 1
        if(not(allZero)):
            if(i != maxRow):
                for j in range(n, col):
                    temp = mat[i, j]
                    mat[i, j] = mat[maxRow, j]
                    mat[maxRow, j] = temp
            divider = mat[i, n]
            for j in range(n, col):
                if(mat[i, j] != 0):
                    mat[i, j] = mat[i, j]/divider
            for j in range(i+1, row):
                t = (-1)*mat[j, n]
                for k in range(n, col):
                    mat[j, k] = mat[j, k] + (t*mat[i, k])
            i += 1
            n += 1
        else:
            n += 1
    return mat

def RRef(mat):
    col = mat.shape[1]

    mat = Ref(mat)
    nonZero = countNonZeroRow(0, col-1, mat)

    for i in range(nonZero-1, -1, -1):
        leadingOneColIdx = getColLeadingNum(mat, i)
        for idx in range(i-1, -1, -1):
            if(mat[idx, leadingOneColIdx] != 0.0):
                num = mat[idx, leadingOneColIdx]
                for j in range(leadingOneColIdx, col):
                    mat[idx, j] = mat[idx, j] - num*mat[i, j]
    return mat

def generateParamVar(numParam):
    cnt = 97
    alpha = np.chararray(numParam)
    for i in range(numParam):
        if(i < 26):
            alpha[i] = chr(cnt+i)
        else:
            for j in range((i//26)+1):
                # TODO: COBA INI
                alpha[i] = chr(alpha[i]) + chr(alpha[i%26])
    return alpha

def printParametric(numParam, mat):
    col = mat.shape[1]

    alpha = generateParamVar(numParam)
    posAlpha = np.full(numParam, -1, dtype=int)

    for i in range(countNonZeroRow(0, col-1, mat)):
        lead = False
        temp = ""
        ans = ["" for i in range(col-1)]

        temp = str(temp) + "x" + str(getColLeadingNum(mat, i)+1) + " ="
        if(mat[i, col-1] != 0):
            temp = str(temp) + " " + str(mat[i, col-1])
            lead = True
        
        for j in range(getColLeadingNum(mat, i)+1, col-1):
            if(mat[i, j] != 0):
                if((-1)*mat[i, j] > 0 and lead):
                    temp = str(temp) + " +"
                else:
                    temp = str(temp) + " "
                cnt = 0
                while (posAlpha[cnt] != j and cnt < numParam and posAlpha[cnt] != -1):
                    cnt += 1
                if(posAlpha[cnt] == -1):
                    posAlpha[cnt] = j
                if(posAlpha[cnt] == j):
                    if((-1)*mat[i, j] == 1):
                        temp = str(temp) + str(alpha[cnt])
                    elif((-1)*mat[i][j] == -1):
                        temp = str(temp) + "-" + str(alpha[cnt])
                    else:
                        temp = str(temp) + str((-1)*mat[i, j]) + str(alpha[cnt])
        ans[getColLeadingNum(mat, i)] = temp
    
    for i in range(col-1):
        if(ans[i] == ""):
            for j in range(numParam):
                if(posAlpha[j] == i):
                    ans[i] = "x" + str(i+1) + " = " + str(alpha[j])
            if(ans[i] == ""):
                j = numParam - 1
                while (posAlpha[j] != -1 and j > 0):
                    j -= 1
                if(posAlpha[j] == -1):
                    ans[i] = "x" + str(i+1) + " = " + str(alpha[j])
                    posAlpha[j] = i
    return ans

def fillMatrix(n, mat):
    row, col = mat.shape
    sq = np.zeros((n, col))
    for i in range(row):
        for j in range(col):
            sq[i, j] = mat[i, j]
    return sq

def segregate(mat, colL, colR):
    row = mat.shape[0]
    col = mat.shape[1]
    mLeft = np.zeros((row, colL))
    for i in range(row):
        for j in range(colL):
            mLeft[i, j] = mat[i, j]

    # return mLeft, mRight
    # mLeft is all we need in this program
    return mLeft

def Determinan(mat):
    row, col = mat.shape
    if(row == 1 and col == 1):
        return mat[0][0]
    else:
        sum = 0.00
        mTemp = np.zeros((row-1, col-1))
        for i in range(col):
            for j in range(1, row):
                c = 0
                for k in range(col):
                    if(k != i):
                        mTemp[j-1, c] = mat[j, k]
                        c += 1
            sum += mat[0, i] * Determinan(mTemp) * math.pow(-1, i)
        return sum

def isInconsistent(mat):
    col = mat.shape[0]
    return (countNonZeroRow(0, col-2, mat) < countNonZeroRow(len(mat[0])-1, col-1, mat))

def cutMatrix(mat, n):
    col = mat.shape[0]
    sq = np.zeros((n, col))

    for i in range(n):
        for j in range(col):
            sq[i, j] = mat[i, j]
    return sq

def GaussJordan(mat):
    row, col = mat.shape
    res = ['' for i in range(col-1)]
    num = np.zeros(col-1)
    consistent = True
    temp = np.zeros((col-1, col))

    if(row <= col-1):
        if(row != col-1):
            temp = fillMatrix(col-1, mat)
        else:
            temp = CopyMatrix(mat)
        print("ini temp")
        print(temp)
        tempDet = np.zeros((row, col-1))
        tempDet = segregate(temp, col-1, 1)
        print("ini tempdet")
        print(tempDet)
        det = Determinan(tempDet)
        print("det")
        print(det)
        temp = RRef(temp)
        print("ini temp habis rref")
        print(temp)
    else:
        newTemp = CopyMatrix(mat)
        newTemp = RRef(newTemp)
        if(isInconsistent(newTemp)):
            res.append("No solution (inconsistent)")
            consistent = False
        else:
            temp = cutMatrix(newTemp, col-1)
            #newDetTemp = CopyMatrix(temp)
            tempDet = segregate(temp, col-1, 1)
            det = Determinan(tempDet)
    if(consistent):
        if(det != 0):
            for i in range(temp.shape[0]):
                num[i] = temp[i, temp.shape[1]-1]
        else:
            if(isInconsistent(temp)):
                res.append("No solution (inconsistent)")
            else:
                res = printParametric(temp.shape[0] - countNonZeroRow(0, temp.shape[1]-1, temp), temp)
    return res, num

def CopyMatrix(mat):
    row, col = mat.shape
    ret = np.zeros((row, col))

    for i in range(row):
        for j in range(col):
            ret[i, j] = mat[i, j]
    
    return ret

def Transpose(mat):
    row, col = mat.shape
    ret = np.zeros((row, col))
    ret = CopyMatrix(mat)

    for i in range(0, row):
        for j in range(0, col):
            ret[j, i] = mat[i, j]
    
    return ret

def MultiplyMatrix(m1, m2):
    row1 = m1.shape[0]
    row2, col2 = m2.shape
    temp = np.zeros((row1, col2))

    for i in range(row1):
        for j in range(col2):
            for k in range(row2):
                temp[i, j] += m1[i, k]*m2[k, j]
    
    return temp

def IdentityMatrix(n):
    ident = np.zeros((n, n))

    for i in range(n):
        ident[i, i] = 1
    
    return ident
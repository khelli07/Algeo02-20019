
# import numpy as np
# from scipy.linalg import hessenberg
# from tabulate import tabulate

# # A is a square random matrix of size n
# n = 5
# A = np.array([[3, -2, 0], [-2, 3, 0], [0, 0, 5]]).astype(float)
# print("A=")
# print(tabulate(A))
# H = hessenberg(A, calc_q=True)

# def eigen_qr_practical(A, iterations=10000):
#     Ak = np.copy(A)
#     n = Ak.shape[0]
#     QQ = np.eye(n)
#     for k in range(iterations):
#         # s_k is the last item of the first diagonal
#         s = Ak.item(n-1, n-1)
#         smult = s * np.eye(n)
#         # pe perform qr and subtract smult
#         Q, R = np.linalg.qr(np.subtract(Ak, smult))
#         # we add smult back in
#         Ak = np.add(R @ Q, smult)
#         QQ = QQ @ Q
#         if k % 10000 == 0:
#             print("A",k,"=")
#             print(tabulate(Ak))
#             print("\n")
#     return Ak, QQ

# #Print results
# eigen_qr_practical(H)

# #Print the results of the "official" numpy algorithm
# print(np.linalg.eigvals(H))

import numpy as np
from tabulate import tabulate

# A is a square random matrix of size n
n = 3
A = np.array([[3, -2, 0], [-2, 3, 0], [0, 0, 5]]).astype(float)
print("A=")
print(tabulate(A))

def eigen_qr_practical(A, iterations=10000):
    Ak = np.copy(A)
    n = Ak.shape[0]
    QQ = np.eye(n)
    for k in range(iterations):
        # s_k is the last item of the first diagonal
        s = Ak.item(n-1, n-1)
        smult = s * np.eye(n)
        # pe perform qr and subtract smult
        Q, R = np.linalg.qr(np.subtract(Ak, smult))
        # we add smult back in
        Ak = np.add(R @ Q, smult)
        QQ = QQ @ Q
        if k % 1000 == 0:
            print("A",k,"=")
            print(tabulate(Ak))
            print("\n")
            print(tabulate(QQ))
            print("\n")
    return Ak, QQ

#Print results
eigen_qr_practical(A)

#Print the results of the "official" numpy algorithm
print(np.linalg.eigvals(A))
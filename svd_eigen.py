import numpy as np

def mat_norm (mat):
    norm = float(np.max(np.sum(np.abs(mat), axis=0)))
    return norm

# def power_iterate (mat)

# def eigen_val (mat):

def power_iteration(A, num_simulations: int):
    # Ideally choose a random vector
    # To decrease the chance that our vector
    # Is orthogonal to the eigenvector
    b_k = np.random.rand(A.shape[1])

    for _ in range(num_simulations):
        # calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)

        # calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)

        # re normalize the vector
        b_k = b_k1 / b_k1_norm

    return b_k

def eigenvalue(A, v):
    # uses property A @ eigenvector = eigenvalue @ eigenvector =>
    # eigenvalue = (A @ eigenvector) / eigenvector
    val = A @ v / v
    return val[0]

def svd_power_iteration(A):
    n, d = A.shape
    #create original normal vector v which is used to approximate dominant eigenvalue
    v = np.ones(A.shape[1])
    ev = eigenvalue(A, v)
    while True:
        #these two lines are basically the core of power iteration
        Av = A @ v
        v_new = Av / np.linalg.norm(Av)
        ev_new = eigenvalue(A, v_new)
        #break if new eigenvalue is not much different from previous
        if np.abs(ev - ev_new) < 0.01:
            break
        v = v_new
        ev = ev_new
    return ev_new, v_new

a = np.array([[3, 0], [8, -1]])

print(power_iteration(a, 10))

eigen_value, eigen_vec = svd_power_iteration(a)

print(eigen_value)
print(eigen_vec)

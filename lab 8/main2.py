import numpy as np


def LU(A, L, U):
    n = len(A)
    U = A.copy()
    for i in range(n):
        for j in range(i, n):
            L[j][i] = U[j][i] / U[i][i]

    for k in range(1, n):
        for i in range(k - 1, n):
            for j in range(i, n):
                L[j][i] = U[j][i] / U[i][i]
        for i in range(k, n):
            for j in range(k - 1, n):
                U[i][j] = U[i][j] - L[i][k - 1] * U[k - 1][j]

    return (L, U)


def LU_method(a, b):
    n = len(a)
    L, U = np.zeros((n, n)), np.zeros((n, n))
    L, U = LU(a, L, U)
    print('L:', L)
    print('U:', U)

    Y = np.zeros(n)
    for i in range(n):
        sum_of = 0
        for p in range(i):
            sum_of += L[i][p] * Y[p]
        Y[i] = b[i] - sum_of
    # print(Y)
    res = np.zeros(n)
    nn=n-1
    for i in range(n):
        sum_of = 0
        for p in range(i):
            sum_of += U[nn - i][nn - p] * res[nn - p]
        res[nn - i] = (1 / U[nn - i][nn - i]) * (Y[nn - i] - sum_of)
    return res


if __name__ == '__main__':
    A = np.array([[15.7, 6.6, -5.7, 11.5],
                  [8.8, -6.7, 5.5, -4.5],
                  [6.3, -5.7, -23.4, 6.6],
                  [14.3, 8.7, -15.7, -5.8]])
    B = np.array([-2.4, 5.6, 7.7, 23.4])

    # A = np.array([[2., 1., 1., 1.],
    #               [2., 4., 0., 0.],
    #               [4., 0., 8., 0.],
    #               [6., 0., 0., 16.]])
    # B = np.array([11., 10., 28., 70.])

    print('Матрица A:', A)
    resUL = LU_method(A, B)
    print('Метод LU разложения:')
    for i in range(len(A)):
        print(resUL[i])

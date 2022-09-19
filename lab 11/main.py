import numpy as np


def LU(A, L, U):
    n = len(A)
    U = A
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


def det_matrix(u):
    det_a = 1
    for i in range(len(u)):
        for j in range(len(u)):
            if i == j:
                det_a *= u[i][j]
    print(f'det A = {det_a}')


def gause(a, y, n):
    a = a.copy()
    eps = 0.00001
    x = np.zeros(n)

    k = 0
    while k < n:
        max = np.abs(a[k][k])
        index = k
        for i in range(k + 1, n):
            if np.abs(a[i][k] > max):
                max = np.abs(a[i][k])
                index = i
        for j in range(n):
            a[k][j], a[index][j] = a[index][j], a[k][j]
        y[k], y[index] = y[index], y[k]

        for i in range(k, n):
            temp = a[i][k]
            if np.abs(temp) < eps:
                continue
            for j in range(n):
                a[i][j] = a[i][j] / temp

            y[i] = y[i] / temp

            if i == k:
                continue
            for j in range(n):
                a[i][j] = a[i][j] - a[k][j]
            y[i] = y[i] - y[k]
        k += 1

    k = n - 1
    while k > -1:
        for i in range(k, -1, -1):
            temp = a[i][k]
            if np.abs(temp) < eps:
                continue
            for j in range(n):
                a[i][j] = a[i][j] / temp
            y[i] = y[i] / temp

            if i == k:
                continue

            for j in range(n):
                a[i][j] = a[i][j] - a[k][j]
            y[i] = y[i] - y[k]
        k -= 1

    for k in range(n - 1, -1, -1):
        x[k] = y[k]
        for i in range(k):
            y[i] = y[i] - a[i][k] * x[k]
    return y


def inverse_matrix(U, L):
    n = len(L)
    E = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                E[i][j] = 1

    Y = np.zeros((n, n), dtype=float)
    for i in range(n):
        Y[i] = gause(L, E[i], n)
        print(Y[i])
    X = np.zeros((n, n), dtype=float)
    for i in range(n):
        X[i] = gause(U, Y[i], n)
    X = np.transpose(X)
    print(X)


def inverse_matrix_gause(a, n):
    eps = 0.00001

    e = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                e[i][j] = 1

    k = 0
    while k < n:
        for i in range(k, n):
            temp = a[i][k]
            if np.abs(temp) < eps:
                continue
            for j in range(n):
                a[i][j] = a[i][j] / temp
                e[i][j] = e[i][j] / temp
            if i == k:
                continue
            for j in range(n):
                a[i][j] = a[i][j] - a[k][j]
                e[i][j] = e[i][j] - e[k][j]
        k += 1

    k = n - 1
    while k > -1:
        for i in range(k, -1, -1):
            tem = a[i][k]
            if np.abs(tem) < eps:
                continue
            for j in range(n):
                a[i][j] = a[i][j] / tem
                e[i][j] = e[i][j] / tem
            if i == k:
                continue
            for j in range(n):
                a[i][j] = a[i][j] - a[k][j]
                e[i][j] = e[i][j] - e[k][j]
        k -= 1
    print(e)


A = np.array([[1, -1, -1, 1],
              [-1, 2, 2, 0],
              [0, -1, 1, 4],
              [1, 1, -1, -1.5]], dtype=float)
n = len(A)
L, U = np.zeros((n, n)), np.zeros((n, n))
A1 = A.copy()
L, U = LU(A1, L, U)
print('U:', U)
print('L', L)

det_matrix(U)

print('Обратная LU метод:')
inverse_matrix(U, L)
print('Обратная Гаусс метод:')
inverse_matrix_gause(A, n)

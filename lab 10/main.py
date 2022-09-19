import numpy as np


def straight_gauss(a, y, n):
    eps = 0.00001

    k = 0
    while k < n:
        for i in range(n):
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
    return y


def reverse_gauss(a, y, n):
    eps = 0.00001

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
    return y


def square_root_method(a, b):
    n = len(a)
    S = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                S[0][0] = np.sqrt(a[0][0])
            elif i == 0 and j > 0:
                S[i][j] = a[i][j] / S[0][0]
            elif i == j and i > 0:
                sum_of = 0
                for k in range(i):
                    sum_of += S[k][i] * S[k][i]
                S[i][i] = np.sqrt(a[i][i] - sum_of)
            elif i < j:
                sum_of = 0
                for k in range(i):
                    sum_of += S[k][i] * S[k][j]
                S[i][j] = (a[i][j] - sum_of) / S[i][i]

    St = S.copy()
    St = np.transpose(St)
    Y = straight_gauss(St, b, 3)
    X = reverse_gauss(S, Y, 3)
    for i in range(n):
        print(f'x{i + 1} = {X[i]}')


if __name__ == '__main__':
    A = np.array([[2.23, -0.71, 0.63],
                  [-0.71, 5.45, -1.34],
                  [0.63, -1.34, 2.77]])
    B = np.array([1.28, 0.64, -0.87])
    square_root_method(A, B)

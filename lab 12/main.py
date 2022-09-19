import numpy as np

A = np.array([[2.93, 1.42, 0, 0],
              [1.42, -2.87, 0.36, 0],
              [0, 0.36, -2.44, 1],
              [0, 0, 3, 4]])
B = np.array([2.48, -0.75, 1.83, 2])


# A = np.array([[2., -1., 0],
#               [5., 4., 2.],
#               [0., 1., -3.]])
# B = np.array([3, 6, 2])


def TDMA(a, b):
    n = len(a)
    y = [a[0][0]]
    alpha = [-a[0][1] / y[0]]
    beta = [b[0] / y[0]]

    for i in range(1, n):
        y.append(a[i][i] + a[i][i - 1] * alpha[i - 1])
        if i < n - 1:
            alpha.append(-a[i][i + 1] / y[i])
        beta.append((b[i] - a[i][i - 1] * beta[i - 1]) / y[i])

    x = np.zeros(n)
    x[-1] = beta[-1]
    for i in range(n - 2, -1, -1):
        x[i] = alpha[i] * x[i + 1] + beta[i]
    print('y: ', y)
    print('alpha: ', alpha)
    print('beta: ', beta)
    print('x :', x)


TDMA(A, B)

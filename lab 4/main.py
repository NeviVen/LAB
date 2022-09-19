import numpy as np
from sympy import diff, symbols

h = 0.2
X0 = -1
Xn = 0


def f_x_(x):
    return x * np.exp(x) + x


if __name__ == '__main__':
    n = Xn - X0 / h + 1
    X = [X0 + h * x for x in np.arange(n)]
    Y = [f_x_(x) for x in X]
    print('X:', X)
    print('Y', Y)
    y_left_formal = [(Y[index_x] - Y[index_x - 1]) / h for index_x in range(1, len(X))]
    y_right_formal = [(Y[index_x + 1] - Y[index_x]) / h for index_x in range(len(X) - 1)]
    y_central_formal = [(Y[index_x + 1] - Y[index_x - 1]) / (2 * h) for index_x in range(1, len(X) - 1)]
    print('Left:', y_left_formal)
    print('Right:', y_right_formal)
    print('Central:', y_central_formal)
    y_second = [(Y[index_x + 1] - 2 * Y[index_x] + Y[index_x - 1]) / h ** 2 for index_x in range(1, len(X) - 1)]
    exact = [x*np.exp(x)+np.exp(x)+1 for x in X]
    exact_second = [x*np.exp(x)+2*np.exp(x) for x in X[1:-1:]]
    print('Exact:', exact)
    print('Second derivative:', y_second)
    print('Second Exact:', exact_second)


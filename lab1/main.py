# Вариант 5 x^2+4*sin(x)
import numpy as np
from math import factorial

from sympy import diff, symbols, sin, limit

X0 = 0
XN = np.pi
H = np.pi / 5
N1 = 4
N2 = 2
points_x = [0.71, 1.54, 3.01]


def f_x_(x):
    return x ** 2 + 4 * np.sin(x)


def L_n_(x, n, table: dict):
    L = 0
    if table[0] >= x:
        for i, value_x in enumerate(table):
            if value_x <= x:
                table = table[i::]
                break

    for index_x in range(n + 1):
        sum = 0
        sum += f_x_(table[index_x])
        for index_x2 in range(n + 1):
            if index_x != index_x2:
                sum *= (x - table[index_x2]) / (table[index_x] - table[index_x2])
        L += sum
    return L


def R_x_(X, n, table):
    x = symbols('x')
    d = diff(x ** 2 + 4 * sin(x))
    for _ in range(N1):
        d = diff(d)
    # print(d)
    # m = 0
    if N1//2 == 0:
        x0 = table[0] / np.pi
        xn = table[-1] / np.pi
    else:
        x0 = (table[0]-np.pi/2) / np.pi
        xn = (table[-1]-np.pi/2) / np.pi

    if x0 == 1:
        m = 4
    elif x0 < 1:
        if xn > 1:
            m = 4
        else:
            m = max([d.evalf(subs={x: a}) for a in [table[0], table[-1]]])
    elif x0 > 1:
        if (np.pi * (table[0] // np.pi + 1)) <= table[-1]:
            m = 4
        elif (table[0] // np.pi)*np.pi == table[0]:
            m = 4
        else:
            m = max([d.evalf(subs={x: a}) for a in [table[0], table[-1]]])
        # m = max([d.evalf(subs={x: a}) for a in table])
        # print(m)

    w_x_ = 1
    for index_x in range(n + 1):
        w_x_ *= X - table[index_x]
    return m / factorial(n + 1) * w_x_


def y_x_x1_(args):
    if len(args) == 2:
        x1, x2 = args
        return (f_x_(x2) - f_x_(x1)) / (x2 - x1)
    else:
        return (y_x_x1_(args[1::]) - y_x_x1_(args[0:-1:])) / (args[-1] - args[0])


def N_n_(x, n, table_x, table_y):
    sum = 0
    for iteration in range(n + 1):
        if iteration == 0:
            sum += table_y[0]
        else:
            y_x = y_x_x1_(table_x[0:iteration + 1:])
            for index_x in range(iteration):
                y_x *= x - table_x[index_x]
            sum += y_x
    return sum


if __name__ == '__main__':
    X = [x for x in np.arange(X0, XN + H, H)]
    Y = [f_x_(x) for x in np.arange(X0, XN + H, H)]
    '''
    print(X)
    print(Y)
    LX = [L_n_(x, N1, X) for x in X]
    print(LX)
    LX = [L_n_(x, N1, X) for x in points_x]
    print(points_x)
    print(LX)
    print('r4(x)<=', R_x_(points_x[2], N1, X))
    '''

    for i, x in enumerate(points_x):
        if X[0] >= x:
            for i, value_x in enumerate(X):
                if value_x <= x:
                    X = X[i::]
                    break
        f = f_x_(x)
        l = L_n_(x, N1, X)
        print(f'{i + 1}. |f(x):', f, '|L(x):', l, '|f(x)-L(x):', abs(f - l), '|r(x):', abs(R_x_(x, N1, X)))

    for i, x in enumerate(points_x):
        if X[0] >= x:
            for i, value_x in enumerate(X):
                if value_x <= x:
                    X = X[i::]
                    break
        f = f_x_(x)
        n = N_n_(x, N1, X, Y)
        print(f'{i + 1}. |f(x):', f, '|N(x):', n, '|f(x)-N(x):', abs(f - n), '|r(x):', abs(R_x_(x, N1, X)))

import numpy as np

h = np.pi / 5
X0 = 0
Xn = np.pi
x_values = [X0 + 0.3, X0 + 0.5 * h, Xn - 0.5 * h]
N = 5


def f_x_(x):
    return x ** 2 + 4 * np.sin(x)


def splynes(Points, X, A, B, C, D):
    spl = []
    for x0 in Points:
        for index, x in enumerate(X):
            if x < x0 < X[index + 1]:

                ind_for_spl = index
                spl.append(
                    A[ind_for_spl] + B[ind_for_spl] * (x0 - X[ind_for_spl + 1]) + C[ind_for_spl] * (
                            x0 - X[ind_for_spl + 1]) ** 2 / 2 + D[ind_for_spl] * (
                            x0 - X[ind_for_spl + 1]) ** 3 / 6)
                break
    return spl


if __name__ == '__main__':
    # X
    print('X0:', x_values)
    X = [x for x in np.arange(X0, Xn + h, h)]
    print('x:', X)

    # A
    Y = [f_x_(x) for x in X]
    print('y:', Y)
    A = Y[1::]
    print('A:', A)
    # C
    mat1, mat2 = [], []
    for i in range(2, N + 1):
        itermas = []
        for ii in range(2, N + 1):
            if i - 1 == ii:
                itermas.append(h)
            elif i == ii:
                itermas.append((h + h) ** 2)
            elif i + 1 == ii:
                itermas.append(h)
            else:
                itermas.append(0)

        mat2.append(6 * ((Y[i] - Y[i - 1]) / h - (Y[i - 1] - Y[i - 2]) / h))
        mat1.append(itermas)

    mat1 = np.array(mat1)
    mat2 = np.array(mat2)

    C = list(np.linalg.solve(mat1, mat2))
    C.append(0)
    C.insert(0, 0)
    #
    # C=[0,-77932142240048270/6660364080768857,5463397489263628/4228835921336193,11521556135134336/8918035077933605,-10931430691677294/10931430691677294,0]
    print('C:', C)
    # D
    D = [(C[i] - C[i - 1]) / h for i in range(1, len(C))]
    print('D:', D)
    # B
    B = []
    for i in range(0, N):

        b = (C[i+1] * h / 2) - (D[i] * h ** 2 / 6) + (Y[i + 1] - Y[i]) / h
        B.append(b)
    print('B:', B)
    # S
    spl = splynes(x_values, X, A, B, C, D)
    print('X0:', x_values)
    print('S:', spl)
    print('Y:', [f_x_(x) for x in x_values])

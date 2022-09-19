import numpy as np

X = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
Y = [6, 3, 1, 0.3, -0.1, -0.2, 0, 0.2, 1]

if __name__ == '__main__':
    # y=ax+b
    mat1 = []
    mat2 = []
    mat = []

    # a
    coefficient = 0
    for x in X:
        coefficient += x ** 2
    mat.append(coefficient)

    # b
    coefficient = 0
    for x in X:
        coefficient += x
    mat.append(coefficient)
    mat1.append(mat)
    coefficient = 0

    # a+b=
    for index_y, x in enumerate(X):
        coefficient += x * Y[index_y]
    mat2.append(coefficient)
    mat = []

    # 2 a
    coefficient = 0
    for x in X:
        coefficient += x
    mat.append(coefficient)

    # 2 b
    coefficient = len(X)
    mat.append(coefficient)
    mat1.append(mat)
    coefficient = 0

    # 2 a+b=
    for y in Y:
        coefficient += y
    mat2.append(coefficient)

    mat1 = np.array(mat1)
    mat2 = np.array(mat2)

    C = list(np.linalg.inv(mat1).dot(mat2))

    print('ax+b : ', f'{C[0]}x+{C[1]}')
    r=[(Y[index_y]-(C[0]*x+C[1]))**2 for index_y,x in enumerate(X)]
    print(sum(r))
    # y=ax^2+bx+c
    mat1 = []
    mat2 = []
    mat = []

    # a
    coefficient = 0
    for x in X:
        coefficient += x ** 4
    mat.append(coefficient)

    # b
    coefficient = 0
    for x in X:
        coefficient += x ** 3
    mat.append(coefficient)
    coefficient = 0

    # c
    coefficient = 0
    for x in X:
        coefficient += x ** 2
    mat.append(coefficient)
    mat1.append(mat)
    coefficient = 0

    # ax+bx+c=
    for index_y, x in enumerate(X):
        coefficient += Y[index_y] * x ** 2
    mat2.append(coefficient)
    mat = []

    # 2a
    coefficient = 0
    for x in X:
        coefficient += x ** 3
    mat.append(coefficient)

    # 2b
    coefficient = 0
    for x in X:
        coefficient += x ** 2
    mat.append(coefficient)

    # 2c
    coefficient = 0
    for x in X:
        coefficient += x
    mat.append(coefficient)
    mat1.append(mat)

    # 2 ax+bx+c=
    coefficient = 0
    for index_y, x in enumerate(X):
        coefficient += Y[index_y] * x
    mat2.append(coefficient)
    mat = []

    # 3a
    coefficient = 0
    for x in X:
        coefficient += x ** 2
    mat.append(coefficient)

    # 3b
    coefficient = 0
    for x in X:
        coefficient += x
    mat.append(coefficient)

    # 3c
    coefficient = len(X)
    mat.append(coefficient)
    mat1.append(mat)

    # 2ax+bx+c=
    coefficient = 0
    for y in Y:
        coefficient += y
    mat2.append(coefficient)

    mat1 = np.array(mat1)
    mat2 = np.array(mat2)

    C = list(np.linalg.inv(mat1).dot(mat2))

    print('ax^2+bx+c : ', f'{C[0]}x^2{C[1]}x{C[2]}')
    r = [(Y[index_y] - (C[0] * x**2 + C[1]*x+C[2])) ** 2 for index_y, x in enumerate(X)]
    print(sum(r))
    # acosx
    xx = 0
    yy = 0
    for index_y, x in enumerate(X):
        xx += np.cos(x)*np.cos(x)
        yy += Y[index_y]*np.cos(x)

    print('acos(x) : ', f'{yy / xx}cos(x)')
    r = [(Y[index_y] - yy/xx*np.cos(x)) ** 2 for index_y, x in enumerate(X)]
    print(sum(r))


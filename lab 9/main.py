import numpy as np


def gause(a, y, n):
    x = np.zeros(n)
    eps = 0.00001

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

    y_i = []

    for i in range(n):
        count = 0
        for j in range(n):
            if a[i][j] != 0:
                count += 1
        if count == 0 and y[i] != 0:
            print('Решений нет')
            return None
        if count == 0 and y[i] == 0:
            y_i.append(i)

    if len(y_i) != 0:
        for i in range(len(y_i)):
            print(f'x{y_i[i] + 1}')
        print('свободные переменные')
        for i in range(n):
            if i in y_i:
                continue
            for j in range(n):
                if j not in y_i:
                    if a[i][j] != 0:
                        print(f' + {a[i][j]}x{j + 1}', end='')
            print(f' = {y[i]}')
            for j in range(n):
                if j in y_i:
                    print(f' - {a[i][j]}x{j + 1}', end='')

        return None

    for k in range(n - 1, -1, -1):
        x[k] = y[k]
        for i in range(k):
            y[i] = y[i] - a[i][k] * x[k]

    for i in range(len(x)):
        print(f'x{i + 1} = {x[i]}')


def jordan_gauss(a, y, n):
    eps = 0.00001
    x=np.zeros(n)

    k = 0
    while k < n:
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

    y_i = []
    # print(a)
    for i in range(n):
        count = 0
        for j in range(n):
            if a[i][j] == 0:
                count += 1
        if count == 0 and y[i] != 0:
            print('Решений нет')
            return None
        if count == 0 and y[i] == 0:
            y_i.append(i)

    if len(y_i) != 0:
        for i in range(len(y_i)):
            print(f'x{y_i[i] + 1}')
        print('свободные переменные')
        for i in range(n):
            if i in y_i:
                continue
            for j in range(n):
                if j not in y_i:
                    if a[i][j] != 0:
                        print(f' + {a[i][j]}x{j + 1}', end='')
            print(f' = {y[i]}')
            for j in range(n):
                if j in y_i:
                    print(f' - {a[i][j]}x{j + 1}', end='')

        return None

    for k in range(n - 1, -1, -1):
        x[k] = y[k]
        for i in range(k):
            y[i] = y[i] - a[i][k] * x[k]

    for i in range(len(x)):
        print(f'x{i + 1} = {x[i]}')




if __name__ == '__main__':
    A = np.array([[3.01, -0.14, -0.15],
                  [1.11, 0.13, -0.75],
                  [0.17, -2.11, 0.71]])
    B = np.array([1., 0.13, 0.17])
    print('Метод гаусса:')
    gause(A.copy(), B.copy(), 3)
    print('Метод Жордана-Гаусса:')
    jordan_gauss(A, B, 3)

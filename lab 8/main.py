import numpy as np

A = np.array([[15.7, 6.6, -5.7, 11.5],
              [8.8, -6.7, 5.5, -4.5],
              [6.3, -5.7, -23.4, 6.6],
              [14.3, 8.7, -15.7, -5.8]])
B = np.array([-2.4, 5.6, 7.7, 23.4])
A = np.array([[1, 2, 3, 4],
              [1, 2, 3, 5],
              [1, 2, 3, 6],
              [1, 2, 3, 7]], dtype=float)
B = np.array([10, 11, 12, 13], dtype=float)
print('Метод Гаусса:')


def gause(a, y, n):
    x = np.zeros(n)
    eps = 0.00001

    k = 0
    while k < n:
        print(f'Столбец {k}\n///////////////')
        max = np.abs(a[k][k])
        index = k
        for i in range(k + 1, n):
            if (np.abs(a[i][k]) > max):
                max = np.abs(a[i][k])
                index = i

        print(f'Меняем строки {index} и {k}')
        print(a)

        for j in range(n):
            a[k][j], a[index][j] = a[index][j], a[k][j]
        print(a)
        y[k], y[index] = y[index], y[k]

        for i in range(k, n):
            temp = a[i][k]
            if (np.abs(temp) < eps):
                continue
            for j in range(n):
                a[i][j] = a[i][j] / temp
            print(f'Делим строку {i} на {temp}')
            print(a)
            y[i] = y[i] / temp
            if i == k:
                continue
            for j in range(n):
                a[i][j] = a[i][j] - a[k][j]
            y[i] = y[i] - y[k]
            print(f'Вычитаем из строки {i} строку {k}')
            print(a)
            print(y)
        print(f'{k}\n//////////////////')
        k += 1

    k = n - 1
    while k > -1:
        for i in range(k, -1, -1):
            tem = a[i][k]
            if np.abs(tem) < eps or a[k][k] == 0:
                continue
            for j in range(n):
                a[i][j] = a[i][j] / tem
            y[i] = y[i] / tem
            print(a)
            if i == k:
                continue
            for j in range(n):
                a[i][j] = a[i][j] - a[k][j]
            y[i] = y[i] - y[k]
            print(a)
        k -= 1

    y_i = []
    print(a)
    for i in range(n):
        count = 0
        for j in range(n):
            if (a[i][j] != 0):
                count += 1
            # print(a[i][j])
        if count == 0 and y[i] != 0:
            print('Нет решений')
        if count == 0 and y[i] == 0:
            y_i.append(i)
    print(len(y_i))
    if (len(y_i) != 0):
        for i in range(len(y_i)):
            print(f'x{y_i[i] + 1}')
        print('Свободная переменные(ая)')
        for i in range(n):
            if (j in y_i):
                continue
            for j in range(n):
                if (j not in y_i):
                    if a[i][j] != 0:
                        print(f' + {a[i][j]}x{j + 1}', end=' ')
            print(f'{y[i]}', end='')
            for j in range(n):
                if j in y_i:
                    print(f' - {a[i][j]}x{j + 1}', end='')
            print()
        return None

    for k in range(n - 1, -1, -1):
        x[k] = y[k]
        for i in range(k):
            y[i] = y[i] - a[i][k] * x[k]
    for i in range(n):
        print(f'{i + 1} = {x[i]}')


gause(A, B, 4)

import numpy as np

A = np.array([[6.25, -1, 0.5],
             [-1, 5, 2.12],
             [0.5, 2.12, 3.6]])
B = np.array([5.75, 6.12, 6.22])

A1 = np.array([[2.93, 1.42, -1.55],
               [1.42, -2.87, 0.36],
               [-1.55, 0.36, -2.44]])
B1 = np.array([2.48, -0.75, 1.83])

def check_diagonal_predominance(matrix):
    n = len(matrix)
    if n == len(matrix[0]):
        for i in range(n):
            sum_of_row_elements = 0
            for j in range(n):
                if i != j:
                    sum_of_row_elements += np.abs(matrix[i][j])
            if sum_of_row_elements > np.abs(matrix[i][i]):
                return False
        return True


def check_end_interation(i, eps=0.001):
    x0, x1 = i[-2], i[-1]
    sub_x = np.zeros(len(x0))
    for i in range(len(x0)):
        sub_x[i] = np.abs(x1[i] - x0[i])
    if max(sub_x) < eps:
        return True
    return False


def scalar_product(a, b):
    sum_of = 0
    for i in range(len(a)):
        sum_of += a[i] * b[i]
    return sum_of


def diff(a, b):
    diff = np.zeros(len(a))
    for i in range(len(a)):
        diff[i] = a[i] - b[i]
    return diff


def multiplication(x, y):
    n = len(x)
    res = np.zeros(n)
    for i in range(len(x)):
        for j in range(len(y)):
            res[i] += x[i][j] * y[j]
    return res


def multiplication_in_value(x, a):
    res = np.zeros(len(x))
    for i in range(len(x)):
        res[i]= x[i]*a
    return res


def relax_method(a, b, fi):
    iteration_result = []
    n = len(a)
    x0 = np.zeros(n)
    for i in range(n):
        x0[i] = b[i] / a[i][i]
    iteration_result.append(x0)

    while_condition = True
    while while_condition:
        x = iteration_result[-1]
        next_x = np.zeros(n)
        for i in range(n):
            sum_of = 0
            for j in range(i):
                if j != i:
                    sum_of += -a[i][j] / a[i][i] * next_x[j]
            for j in range(i, n):
                if j != i:
                    sum_of += -a[i, j] / a[i][i] * x[j]
            next_x[i] = fi * (sum_of + b[i] / a[i][i]) - x[i] * (fi - 1)
        iteration_result.append(next_x)
        if check_end_interation(iteration_result):
            while_condition = False
    res_x = iteration_result[-1]
    print(f'Итераций: {len(iteration_result) - 1}')
    for i in range(n):
        print('{0:0.4f}'.format(res_x[i]))


def method_rapid_descent(a, b):
    iteration_result = []
    n = len(a)
    x0 = np.zeros(n)
    iteration_result.append(x0)
    while_condition = True
    while while_condition:
        x = iteration_result[-1]
        r = diff(multiplication(a, x), b)
        t = scalar_product(r, r) / scalar_product(multiplication(a, r), r)
        next_x = diff(x, multiplication_in_value(r, t))
        iteration_result.append(next_x)
        # print(x)
        if check_end_interation(iteration_result):
            while_condition = False
    res_x = iteration_result[-1]
    print(f'Итераций: {len(iteration_result) - 1}')
    for i in range(n):
        print('{0:0.4f}'.format(res_x[i]))


if __name__ == '__main__':
    print('Метод релаксации:')
    relax_method(A, B, 1.2)
    print('Метод скорейшего спуска:')
    method_rapid_descent(A, B)

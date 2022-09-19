import numpy as np

# A = np.array([[10, 1, 1],
#               [2, 10, 1],
#               [2, 2, 10]])
# B = np.array([12, 13, 14])
A = np.array([[5.3, 2.1, 2.8],
              [2.1, 4.7, 1.8],
              [2.7, 1.8, 6.1]])
B = np.array([0.8, 5.7, 3.2])


def check_end_interation(i, eps=0.001):
    x0, x1 = i[-2], i[-1]
    sub_x = np.zeros(len(x0))
    for i in range(len(x0)):
        sub_x[i] = np.abs(x1[i] - x0[i])
    if max(sub_x) < eps:
        return True
    return False


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


def jacobi_methid(a, b):
    n = len(a)
    iteration_result = []
    x0 = np.zeros(n)
    for i in range(n):
        x0[i] = b[i] / a[i][i]
    iteration_result.append(x0)
    condition_while = True

    while condition_while:
        x = iteration_result[-1]
        next_x = np.zeros(n)
        for i in range(n):
            sum_of = 0
            for j in range(n):
                if i != j:
                    sum_of += a[i][j] * x[j] / a[i][i]
                next_x[i] = -sum_of + b[i] / a[i][i]
        iteration_result.append(next_x)
        if check_end_interation(iteration_result):
            condition_while = False
    res_x = iteration_result[-1]
    print(f'Итераций: {len(iteration_result) - 1}')
    for i in range(n):
        print('{0:0.4f}'.format(res_x[i]))


def check_convergence_condition(matrix):
    n = len(matrix)
    b = np.zeros(n)
    for i in range(n):
        sum_of = 0
        for j in range(n):
            if i != j:
                sum_of += np.abs(matrix[i][j] / matrix[i][i])
        b[i] = sum_of
    if max(b) < 1:
        return True
    return False


def seidel_method(a, b):
    n = len(a)
    iteration_result = []
    x0 = np.zeros(n)
    for i in range(n):
        x0[i] = b[i] / a[i][i]
    # x0[-1],x0[-2]=0,0
    iteration_result.append(x0)

    condition_while = True
    while condition_while:
        x = iteration_result[-1]
        next_x = np.zeros(n)
        for i in range(n):
            sum_of = 0
            for j in range(i):
                if j != i:
                    sum_of += -a[i][j] * next_x[j] / a[i][i]
            for j in range(i, n):
                if j != i:
                    sum_of += -a[i][j] * x[j] / a[i][i]
            next_x[i] = sum_of + b[i] / a[i][i]

        iteration_result.append(next_x)
        if check_end_interation(iteration_result):
            condition_while = False
    res_x = iteration_result[-1]
    print(f'Итераций: {len(iteration_result) - 1}')
    for i in range(n):
        print('{0:0.4f}'.format(res_x[i]))


if __name__ == '__main__':
    print('Метод Якоби:')
    if check_diagonal_predominance(A):
        print(True)
        jacobi_methid(A, B)
    else:
        print(False)
    print('Метод Зейделя:')
    if check_convergence_condition(A):
        print(True)
        seidel_method(A, B)
    else:
        print(False)

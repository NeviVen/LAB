import numpy as np

print(np.exp(1))
a = 0
b = 1
h = 0.1
n = 10

alpha_1 = 1
alpha_2 = 1
beta_1 = 0
beta_2 = 0
gamma_1 = 0
gamma_2 = np.exp(1)


def xi(i):
    # print(x0 + i * h)
    return a + i * h


def Y_0(x, y, z):
    return z


def Y_1(x, y, z):
    return z


def Y_2(x, y, z):
    return z


def S_0(x, y, z):
    return -2 * x * np.exp(x) + 2 * z + y


def S_1(x, y, z):
    return 2 * z + y


def S_2(x, y, z):
    return 2 * z + y


def Y0(x, y, z):
    k_1 = Y_0(x, y, z)
    l_1 = S_0(x, y, z)
    k_2 = Y_0(x + h / 2, y + h / 2 * k_1, z + h / 2 * l_1)
    l_2 = S_0(x + h / 2, y + h / 2 * k_1, z + h / 2 * l_1)
    k_3 = Y_0(x + h / 2, y + h / 2 * k_2, z + h / 2 * l_2)
    l_3 = S_0(x + h / 2, y + h / 2 * k_2, z + h / 2 * l_2)
    k_4 = Y_0(x + h, y + h * k_3, z + h * l_3)
    l_4 = S_0(x + h, y + h * k_3, z + h * l_3)
    return (y + 1 / 6 * h * (k_1 + 2 * k_2 + 2 * k_3 + k_4), z + 1 / 6 * h * (l_1 + 2 * l_2 + 2 * l_3 + l_4))


def Y1(x, y, z):
    k_1 = Y_1(x, y, z)
    l_1 = S_1(x, y, z)
    k_2 = Y_1(x + h / 2, y + h / 2 * k_1, z + h / 2 * l_1)
    l_2 = S_1(x + h / 2, y + h / 2 * k_1, z + h / 2 * l_1)
    k_3 = Y_1(x + h / 2, y + h / 2 * k_2, z + h / 2 * l_2)
    l_3 = S_1(x + h / 2, y + h / 2 * k_2, z + h / 2 * l_2)
    k_4 = Y_1(x + h, y + h * k_3, z + h * l_3)
    l_4 = S_1(x + h, y + h * k_3, z + h * l_3)
    return (y + 1 / 6 * h * (k_1 + 2 * k_2 + 2 * k_3 + k_4), z + 1 / 6 * h * (l_1 + 2 * l_2 + 2 * l_3 + l_4))


def Y2(x, y, z):
    k_1 = Y_2(x, y, z)
    l_1 = S_2(x, y, z)
    k_2 = Y_2(x + h / 2, y + h / 2 * k_1, z + h / 2 * l_1)
    l_2 = S_2(x + h / 2, y + h / 2 * k_1, z + h / 2 * l_1)
    k_3 = Y_2(x + h / 2, y + h / 2 * k_2, z + h / 2 * l_2)
    l_3 = S_2(x + h / 2, y + h / 2 * k_2, z + h / 2 * l_2)
    k_4 = Y_2(x + h, y + h * k_3, z + h * l_3)
    l_4 = S_2(x + h, y + h * k_3, z + h * l_3)
    return (y + 1 / 6 * h * (k_1 + 2 * k_2 + 2 * k_3 + k_4), z + 1 / 6 * h * (l_1 + 2 * l_2 + 2 * l_3 + l_4))


def u_x(y0, y1, y2):
    return y0 + c1 * y1 + c2 * y2


y = 0
z = 0
print(f'{xi(0)}\t|\t{y}\t|\t{z}', end='')
y_0, z_0 = np.zeros(n+1), np.zeros(n+1)
y_0[0] = y
z_0[0] = z
for i in range(1,n+1):
    x = xi(i)

    y_0[i], z_0[i] = Y0(x, y, z)
    y, z = y_0[i], z_0[i]
    print(f'\n{x + h}\t|', y, '\t|', z, end='')
print('\n\n\n')
y = 1
z = 0
print(f'{xi(0)}\t|\t{y}\t|\t{z}', end='')
y_1, z_1 = np.zeros(n+1), np.zeros(n+1)
y_1[0] = y
z_1[0] = z
for i in range(1,n+1):
    x = xi(i)

    y_1[i], z_1[i] = Y1(x, y, z)
    y, z = y_1[i], z_1[i]
    print(f'\n{x + h}\t|', y, '\t|', z, end='')
print('\n\n\n')
y = 0
z = 1
print(f'{xi(0)}\t|\t{y}\t|\t{z}', end='')
y_2, z_2 = np.zeros(n+1), np.zeros(n+1)
y_2[0] = y
z_2[0] = z
for i in range(1,n+1):
    x = xi(i)

    y_2[i], z_2[i] = Y2(x, y, z)
    y, z = y_2[i], z_2[i]
    print(f'\n{x + h}\t|', y, '\t|', z, end='')

matrix = np.array([[alpha_1, beta_1],
                   [alpha_2 * y_1[-1] + beta_2 * z_1[-1], alpha_2 * y_2[-1] + beta_2 * z_2[-1]]])
dop_matrix = np.array([gamma_1, gamma_2-alpha_2*y_0[-1]-beta_2*z_0[-1]])
c1, c2 = np.linalg.solve(matrix, dop_matrix)
# c2 = 1
# c1 = (gamma_2 - y_0[-1] - c2 * y_2[-1]) / y_1[-1]

print('\n\n\n', [xi(i) * np.exp(xi(i)) for i in range(n+1)])
print([u_x(y_0[i], y_1[i], y_2[i]) for i in range(n+1)])

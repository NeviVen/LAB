# example2

n = 5
X0 = 0
Xn = 1
h = 0.2


def xi(x0, i, h):
    # print(x0 + i * h)
    return x0 + i * h


def f_x(x, y, z):
    return z


def g_x(x, y, z):
    return 2 * x * z / (x ** 2 + 1)


def l_k(x, y, z):
    k_1 = f_x(x, y, z)
    l_1 = g_x(x, y, z)
    k_2 = f_x(x + h / 2, y + h / 2 * k_1, z + h / 2 * l_1)
    l_2 = g_x(x + h / 2, y + h / 2 * k_1, z + h / 2 * l_1)
    k_3 = f_x(x + h / 2, y + h / 2 * k_2, z + h / 2 * l_2)
    l_3 = g_x(x + h / 2, y + h / 2 * k_2, z + h / 2 * l_2)
    k_4 = f_x(x + h, y + h * k_3, z + h * l_3)
    l_4 = g_x(x + h, y + h * k_3, z + h * l_3)
    return (y + 1 / 6 * h * (k_1 + 2 * k_2 + 2 * k_3 + k_4), z + 1 / 6 * h * (l_1 + 2 * l_2 + 2 * l_3 + l_4))


y = 1
z = 3
print('\t'*2,'y','\t'*5,'z')
print(y,'\t'*4,'   |',z)
for i in range(n):
    x = xi(X0, i, h)

    y, z = l_k(x, y, z)

    print( y,'\t|', z)

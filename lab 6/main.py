# example 1
A = 0
B = 1
n = 10
h = 0.1


# print(1+0.1*(0-2))

def f(x, y):
    # print(x ** 2 - 2 * y)
    return x ** 2 - 2 * y


def x(x0, i, h):
    # print(x0 + i * h)
    return x0 + i * h


# method 1 метод Эйлера
def method_1(x, y, h):
    # print(y + h * f(x, y))
    return y + h * f(x, y)


y0 = 1
method_1_list = []
yi = y0
for i in range(n):
    yi = method_1(x(0, i, h), yi, h)
    method_1_list.append(yi)

print(method_1_list)


# method 2 Усовершенствованый метод эйлера
def method_2(x, y, h):
    return y + h * f(x + h / 2, y + h / 2 * f(x, y))


y0 = 1
method_2_list = []
yi = y0
for i in range(n):
    yi = method_2(x(0, i, h), yi, h)
    method_2_list.append(yi)

print(method_2_list)

# method 3 Трапеций
y0 = 1


def method_3(x, y, h):
    return y + h / 2 * (f(x, y) + f(x + h, method_1(x, y, h)))


y0 = 1
method_3_list = []
yi = y0
for i in range(n):
    yi = method_3(x(0, i, h), yi, h)
    method_3_list.append(yi)

print(method_3_list)


# method 4 Рунге_Кутты
def method_4(x, y, h):
    k1 = f(x, y)
    # print(k1)
    k2 = f(x + h / 2, y + h / 2 * k1)
    # print(k2)
    k3 = f(x + h / 2, y + h / 2 * k2)
    # print(k3)
    k4 = f(x + h, y + h * k3)
    # print(k4)
    return y + 1 / 6 * h * (k1 + 2 * k2 + 2 * k3 + k4)

y0 = 1
method_4_list = []
yi = y0
for i in range(n):
    yi = method_4(x(0, i, h), yi, h)
    method_4_list.append(yi)

print(method_4_list)
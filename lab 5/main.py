import numpy as np

n = 10
X0 = 2
Xn = 3


def f_x_(x):
    return 1/np.cos(x)**2
    return np.log(x)**2/x


if __name__ == '__main__':
    h = (Xn - X0) / n
    hh = (Xn - X0) / (2 * n)
    S_left = h * sum([f_x_(X0 + h * x) for x in np.arange(n)])
    S_right = h * sum([f_x_(X0 + h * x) for x in np.arange(1, n + 1)])
    S_central = h * sum([f_x_(X0 + h * x + h / 2) for x in np.arange(n)])
    S_trapezoid = h / 2 * (2 * sum([f_x_(X0 + h * x) for x in np.arange(1, n)]) + f_x_(X0) + f_x_(Xn))

    S_parabola = hh / 3 * (
            f_x_(X0) + 4 * sum([f_x_(X0 + hh * x) for x in np.arange(1, 2 * n + 1, 2)]) + 2 * sum(
        [f_x_(X0 + hh * x) for x in np.arange(2, 2 * (n - 1) + 1, 2)]) + f_x_(
        2 * n * hh + X0))
    print('S left:', S_left)
    print('S right:', S_right)
    print('S central:', S_central)
    print('S trapezoid:', S_trapezoid)
    print('S parabola:', S_parabola)
    B = Xn
    A = X0
    x = [0.93247, 0.66121, 0.23862]
    c = [0.17132449, 0.36076157, 0.46791393]
    S_g = (B - A) / 2 * (sum([c[i] * f_x_((B - A) / 2 * x[i] + (B + A) / 2) for i in range(len(x))]) + sum(
        [c[i] * f_x_((B - A) / 2 * (-x[i]) + (B + A) / 2) for i in range(len(x))]))

    print('S Gauss', S_g)
    answer=np.log(Xn) ** 3 / 3 - np.log(X0) ** 3 / 3
    print('S Newton-Leibniz', answer)

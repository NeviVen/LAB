import numpy as np

n = 10
a = 0
b = 1
h = (b - a) / n


x = lambda i: i * h + a
p = lambda x: -2
q = lambda x: -1
f = lambda x: -2 * x * np.exp(x)
alpha_1 = 1
alpha_2 = 1
beta_1 = 0
beta_2 = 0
gamma_1 = 0
gamma_2 = np.exp(1)


mat = []
dop_matrix=[]
dop_matrix.append(gamma_1)
added_matrix = np.zeros(n + 1)
added_matrix[0] = alpha_1 - beta_1 / h
added_matrix[1] = beta_1 / h
mat.append(added_matrix)
for i in range(1, n):
    added_matrix = np.zeros(n + 1)
    added_matrix[i - 1] = 1 - h * p(x(i)) / 2
    added_matrix[i] = -2 + h ** 2 * q(x(i))
    added_matrix[i + 1] = 1 + h * p(x(i)) / 2
    mat.append(added_matrix)
    dop_matrix.append(f(x(i))*0.01)
added_matrix = np.zeros(n + 1)
added_matrix[-2] = -beta_2 / h
added_matrix[-1] = alpha_2 + beta_2 / h
mat.append(added_matrix)
dop_matrix.append(gamma_2)
mat=np.array(mat)
dop_matrix=np.array(dop_matrix)

solve=np.linalg.inv(mat).dot(dop_matrix)
print([x(i) for i in range(n+1)])

print([x for x in solve])
print([x(i)*np.exp(x(i)) for i in range(1,n+1)])

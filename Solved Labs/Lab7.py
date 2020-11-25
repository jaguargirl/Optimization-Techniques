import numpy as np
import random

def ke(a, x, b, k):
    print("Kazmartz Extins")
    y = b
    for k_i in range(k):
        for j in range(n):
            y = y-(np.dot(a[:, j], y))/(np.linalg.norm(a[:, j])**2)*a[:, j]
        b_tilda = b-y
        for idx in range(m):
            x = x-(np.dot(x, a[idx].T)-b_tilda[idx])/(np.linalg.norm(a[idx].T)**2)*a[idx].T
        print("X_ls ",x)


def ka(a, x, b, k):
    print("Kazmartz")
    for k_i in range(k):
        for idx in range(m):
            x = x - (np.dot(x, a[idx].T) -b[i])/ (np.linalg.norm(a[idx].T) ** 2) * a[idx].T
        print("X_ls= ", x)

def kerp(a, x, b, k):
    print("Kerp")
    y = b
    for k_i in range(k):
        for j in range(n):
            y = (1 - a[:, j]) * y +a[:, j]*(y - (np.dot(a[:, j], y)) / (np.linalg.norm(a[:, j]) ** 2) * a[:, j])
        b_tilda = b-y
        for idx in range(m):
            omega = 1/(idx+1)
            x = (1 - omega) * x + omega * (x - (np.dot(x, a[idx].T) - b_tilda[idx]) / (np.linalg.norm(a[idx].T) ** 2) * a[idx].T)
        print("X_ls= ",x)

def cimmino(a, x, b, k):
    print("Cimmino")
    y = b
    for k_i in range(k):
        for j in range(n):
            y = (1 - a[:, j]) * y + a[:, j] * (y - (np.dot(a[:, j], y)) / (np.linalg.norm(a[:, j]) ** 2) * a[:, j])
        b_tilda = b-y
        for idx in range(1,m):
            x = x - 2 + (np.dot(x, a[idx].T)-b_tilda[idx])/(np.linalg.norm(a[idx].T)**2)*a[idx].T
        print("X_ls= ",x)

n = int(input("Introduce matrix dimension n= "))
m = n+1
A_matrix = np.zeros((m, n))

# Metoda cu for
for i in range(m):
    if i < n:
        A_matrix[i][i] = 2
    if i == 0:
        A_matrix[i][i+1] = -1
    elif i == n-1:
        A_matrix[i][i-1] = -1
    elif i == n:
        A_matrix[i][0] = 1
        A_matrix[i][n-1] = 1
    else:
        A_matrix[i][i-1] = -1
        A_matrix[i][i+1] = -1

b_vector = np.zeros(m)
b_vector[0] = 1
b_vector[n-1] = 1
b_vector[n] = 2
x_vector = np.zeros(n)
k_iter = int(input("Introduce max nr of iterations k= "))

ke(A_matrix, x_vector, b_vector, k_iter)
ka(A_matrix, x_vector, b_vector, k_iter)
kerp(A_matrix, x_vector, b_vector, k_iter)
cimmino(A_matrix, x_vector, b_vector, k_iter)



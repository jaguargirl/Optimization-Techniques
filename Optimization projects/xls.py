import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry import LineString


def project(point, y_dr):
    global ax
    global x
    new_point = Point(point[0], point[1])
    line = LineString([(x[0], y_dr[0]), (x[99], y_dr[99])])
    xc = np.array(new_point.coords[0])
    uc = np.array(line.coords[0])
    vc = np.array(line.coords[len(line.coords) - 1])
    nc = vc - uc
    nc /= np.linalg.norm(nc)
    P = uc + nc * np.dot(xc - uc, nc)
    return P

def ke(a, xls, b):
    global h1
    global h2
    k = int(input("Introduce max nr of iterations k= "))
    y = b
    for k_i in range(k):
        old_xls = xls
        for j in range(n):
            y = y-(np.dot(a[:, j], y))/(np.linalg.norm(a[:, j])**2)*a[:, j]
        b_tilda = b-y
        for idx in range(m):
            xls = xls-(np.dot(xls, a[idx].T)-b_tilda[idx])/(np.linalg.norm(a[idx].T)**2)*a[idx].T
        ax.plot(xls[0], xls[1], 'co')


n = int(input("Introduce matrix dimension n= "))
m = n+1
A_matrix = np.zeros((m, n))

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

x_vector = [-0.5, -4]
xx = np.linspace(-2, 4, 100)
x = np.zeros(100)
for i in range(100):
    x[i] = xx[i]
h1 = (A_matrix[0][0] * x - b_vector[0])/(-A_matrix[0][1])
h2 = (A_matrix[1][0] * x - b_vector[1])/(-A_matrix[1][1])
fig, ax = plt.subplots()
ax.plot(x, h1, 'b-')
ax.plot(x, h2, 'g-')
ax.plot(x_vector[0], x_vector[1], 'r*', linewidth=2)
pct = project(x_vector, h1)
x_01 = [x_vector[0], int(pct[0])]
y_01 = [x_vector[1], int(pct[1])]
ax.plot(x_01, y_01, 'm-')
x_vector = pct
ke(A_matrix, x_vector, b_vector)
plt.legend(['h1', 'h2', "x0", "x01", "xls"])
plt.title("Xls calculation")
plt.show()




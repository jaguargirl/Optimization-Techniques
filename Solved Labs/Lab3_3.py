import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits import mplot3d

def func(coef, x ,y):
    rez = coef[0] + coef[1] * x + coef[2] * y + coef[3] * x * y
    return  rez

dataset = pd.read_csv('date.csv')
t1 = dataset['x1'].values.reshape(-1, 1)
t2 = dataset['x2'].values.reshape(-1, 1)
b = dataset['Y2_normalizat'].values.reshape(-1, 1)
m = len(t1)

A = np.ones((m, 1))
A = np.hstack((A, t1))
A = np.hstack((A, t2))
A = np.hstack((A, t1 * t2))
x = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, b))
x = x[::-1]

er1 = np.dot(A, x)
er2 = np.linalg.norm((er1 - b))
erf = np.dot(er2, er2)

x1 = np.linspace(min(t1), max(t1), 40)
y1 = np.linspace(min(t2), max(t2), 40)
x2, y2 = np.meshgrid(x1, y1)

z = func(x, x2, y2)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x2, y2, z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

print('Error: ', erf)

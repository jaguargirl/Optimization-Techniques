import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from random import randint
import math
import random


def trH(n, x):
    print(x)
    k = randint(0, n-1)
    print(k)
    I = np.eye(n)
    v = x-np.linalg.norm(x)*I[:, k]
    print(v)
    PvX = x-(np.dot(x, v)/np.linalg.norm(v)**2)*v
    print(PvX)
    if n == 2:
        fig, ax = plt.subplots()
        ax.quiver(x[0], x[1], scale=1, units='xy', color='blue')
        ax.quiver(v[0], v[1], scale=1, units='xy', color="purple")
        ax.quiver(PvX[0], PvX[1], scale=1, units='xy', color="green")
        ax.axis([-7, 7, -7, 7])
        ax.legend(["x", "v", "PvX"])
        plt.title("Householder transformation, n=2")
    else:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.quiver(0, 0, 0, x[0], x[1], x[2], length=0.1, normalize=True, color='blue')
        ax.quiver(0, 0, 0, v[0], v[1], v[2], length=0.1, normalize=True, color="purple")
        ax.quiver(0, 0, 0, PvX[0], PvX[1], PvX[2], length=0.1, normalize=True, color="green")
        ax.legend(["x", "v", "PvX"])
        plt.title("Householder transformation, n=3")
    plt.show()


def trG(n, x):
    teta = math.pi/3
    c = np.cos(teta)
    s = np.sin(teta)
    J = np.eye(n)
    while True:
        i = randint(0, n-1)
        k = randint(0, n-1)
        if i < k:
            break
    J[i][i] = c
    J[k][k] = c
    J[i][k] = -s
    J[k][i] = s
    print(J)
    if n == 2:
        fig, ax = plt.subplots()
        ax.quiver(x[0], x[1], scale=1, units='xy', color='blue')
        ax.axis([-7, 7, -7, 7])
        jx = np.dot(J, x)
        print(jx)
        ax.quiver(jx[0], jx[1], scale=1, units='xy', color="purple")
        ax.legend(["x", "Jx"])
        plt.title("Givens transformation, n=2")
    else:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.quiver(0, 0, 0, x[0], x[1], x[2], length=0.1, normalize=True, color='blue')
        jx = np.dot(J, x)
        ax.quiver(0, 0, 0, jx[0], jx[1], jx[2], length=0.1, normalize=True, color="green")
        ax.legend(["x", "jx"])
        plt.title("Givens transformation, n=3")
        

while True:
    n = int(input("Give n: "))
    if n != 2 and n != 3:
        print("n needs to be 2 or 3")
    else:
        break
while True:
    t = input("Give transformation type (H or G): ")
    if t != 'H' and t != 'G':
        print("Transformation type needs to be H or G")
    else:
        break

if n == 2:
    x = np.zeros(n)
    pct = (input("Give x1 si x2: "))
    x[0], x[1] = pct.split(" ")
    if t == "H":
        trH(n, x)
    else:
        trG(n, x)
elif n == 3:
    x = np.zeros(n)
    pct = (input("Give x1, x2 si x3: "))
    x[0], x[1], x[2] = pct.split(" ")
    if t == "H":
        trH(n, x)
    else:
        trG(n, x)

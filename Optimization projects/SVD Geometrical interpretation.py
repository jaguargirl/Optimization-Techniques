import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits import mplot3d
from matplotlib import cm


def cerc_elipsa():
    n = 2
    A = np.random.random((n, n))
    U, s, Vt = np.linalg.svd(A)
    fi = np.arange(0, 2*math.pi, 0.01)
    k = fi.shape[0]
    x = np.zeros((k, 1))
    for i in range(k):
        x[i] = math.cos(fi[i])
    y = np.zeros((k, 1))
    for i in range(k):
        y[i] = math.sin(fi[i])
    fig = plt.figure()
    plt.plot(x, y, "b-")
    V_ext = np.zeros((n, n+1))
    V_ext[:, 0] = Vt.T[:, 0]
    V_ext[:, 1] = np.zeros(2)
    V_ext[:, 2] = Vt.T[:, 1]
    plt.plot(V_ext[0, :], V_ext[1, :], "g-")
    plt.title("Interpretarea geometrica a teoremei SVD cu n=2")
    plt.legend(["Cercul unitate", "v1,v2"], loc='upper right')
    
    U_tilda = np.zeros((n, n))
    U_tilda[:, 0] = s[0]*U[:, 0]
    U_tilda[:, 1] = s[1]*U[:, 1]
    
    U_ext = np.zeros((n, n+1))
    U_ext[:, 0] = U_tilda[:, 0]
    U_ext[:, 1] = np.zeros(2)
    U_ext[:, 2] = U_tilda[:, 1]
    fig1 = plt.figure()
    plt.plot(U_ext[0, :], U_ext[1, :], "r-")
    
    x_e = np.zeros((k, 1))
    for i in range(k):
        x_e[i] = s[0]*math.cos(fi[i])
    y_e = np.zeros((k, 1))
    for i in range(k):
        y_e[i] = s[1]*math.sin(fi[i])
    
    plt.plot(x_e, y_e, "m-")
    plt.legend(["v3,v4", "Elipsa"], loc='upper right')
    plt.show()


def sfera_elipsoid():
    n = 3
    # A = np.random.random((n, n))
    #A = np.reshape(np.array([0.7, -0.7, 0, 0, 0, 1, 0.7, 0.7, 0]), (3, 3))
    #U, s, Vt = np.linalg.svd(A)
    U = V = np.reshape(np.array([0.7, -0.7, 0, 0, 0, 1, 0.7, 0.7, 0]), (3, 3))
    s= np.array([3, 2, 1])
    
    fi = np.linspace(0,2*math.pi,100)
    teta = np.linspace(0, math.pi, 100)
    k = fi.shape[0]
    
    x = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            x[i][j] = math.sin(teta[i])*math.cos(fi[j])
    
    y = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            y[i][j] = math.sin(teta[i])*math.sin(fi[j])
    
    z = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            z[i][j] = math.cos(teta[i])
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(x, y, z, 50, cmap=cm.PiYG)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title("Interpretarea geometrica a teoremei SVD cu n=3")
    V_ext = np.zeros((n, n+2))
    V_ext[:, 0] = V[:, 0]
    V_ext[:, 1] = np.zeros(n)
    V_ext[:, 2] = V[:, 1]
    V_ext[:, 3] = np.zeros(n)
    V_ext[:, 4] = V[:, 2]
    print(V_ext)
    fig2 = plt.figure()
    axx = plt.axes(projection='3d')
    axx.plot3D(V_ext[0, :], V_ext[1, :], V_ext[2, :], 'b-')
    plt.title("v1, v2, v3 ale sferei")
    plt.show()
    
    x_e = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            x_e[i][j] = s[0]*math.sin(teta[i])*math.cos(fi[j])

    y_e = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            y_e[i][j] = s[1]*math.sin(teta[i])*math.sin(fi[j])
    
    z_e = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            z_e[i][j] = s[2]*math.cos(teta[i])
    
    fig = plt.figure()
    ax_e = plt.axes(projection='3d')
    ax_e.contour3D(x_e, y_e, z_e, 30, cmap=cm.coolwarm)
    ax_e.set_xlabel('x')
    ax_e.set_ylabel('y')
    ax_e.set_zlabel('z')
    plt.title("Elipsoid nerotit")
        
    U_tilda = np.zeros((n, n))
    U_tilda[:, 0] = s[0]*U[:, 0]
    U_tilda[:, 1] = s[1]*U[:, 1]
    U_tilda[:, 2] = s[2]*U[:, 2]
    print(U_tilda)
    U_ext = np.zeros((n, n+2))
    U_ext[:, 0] = U_tilda[:, 0]
    U_ext[:, 1] = np.zeros(n)
    U_ext[:, 2] = U_tilda[:, 1]
    U_ext[:, 3] = np.zeros(n)
    U_ext[:, 4] = U_tilda[:, 2]
    fig = plt.figure()
    axx = plt.axes(projection='3d')
    axx.plot3D(U_ext[0, :], U_ext[1, :], U_ext[2, :], 'g-')
    plt.title("Axele v1, v2, v3 ale elipsoidului")
    plt.show()

    
n = int(input("Introduceti dimensiunea matricei n= "))
if n == 2:
    cerc_elipsa()
elif n == 3:
    sfera_elipsoid()

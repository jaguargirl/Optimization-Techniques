import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD
import time as t

def eigenvalues_eig(a):
    mean = np.zeros((10304, 1))
    mean[:, 0] = a.mean(1)
    o = np.ones((1, 10))
    a = a - np.dot(mean, o)
    L = np.dot(a.T, a)
    t0 = t.perf_counter()
    hqb, d = np.linalg.eig(L)
    t1 = t.perf_counter()
    print("Execution time for eig, t=", t1-t0)
    proiections = np.dot(a, hqb)
    photo = np.reshape(proiections, (112, 92))
    plt.imshow(photo, cmap='gray')
    title = "Eigenfaces with eig, ex_time =" + str(t1 - t0)
    plt.title(title)
    plt.show()


def eigenvalues_svd(a, k):
    t0 = t.perf_counter()
    svd = TruncatedSVD(k)
    svd.fit(a.T)
    t1 = t.perf_counter()
    components = svd.components_
    components = components[:1]
    comp = components.reshape(112, 92)
    plt.imshow(comp, cmap='gray')
    title = "Eigenfaces with TruncatedSVD, k="+str(k)+", timp_ex="+str(t1-t0)
    plt.title(title)
    plt.show()
    print("Execution time for SVD, with k=", k, ", t=", t1-t0)


def create_matrix(nr):
    a = np.zeros((10304, nr))
    for i in range(nr):
        photo = cv2.imread('s15/'+str(i+1)+'.pgm')
        photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
        photo = np.reshape(photo, (10304))
        a[:, i] = photo
    return a

nr =10
A_matrix = create_matrix(10)
k = int(input("Truncated value k= "))
eigenvalues_svd(A_matrix, k)
eigenvalues_eig(A_matrix)

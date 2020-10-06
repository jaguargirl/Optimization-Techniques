import numpy as np
import os
from collections import Counter
from numpy.linalg import norm

t = ["bebelusi", "calculator", "licenta", "apa", "potabila", "odihna", "mici"]
#baza de date
def dataSet(n):
    termeni = t
    m = len(termeni)
    A = np.zeros((m, n))
    fisiere = []
    folder = "E:/OneDrive - Universitatea „OVIDIUS”/Univ/Info3/Tehnici de optimizare/dataSet"
    j = 0
    for file in os.listdir(folder):
        fisiere.append(file)
        filepath = os.path.join(folder, file)
        f = open(filepath, 'r')
        wordcount = Counter(f.read().split())
        for i in range(0, m):
            nr = wordcount[termeni[i]]
            A[i, j] = nr
        f.close()
        j += 1
    print(A)
    U, s, Vt = np.linalg.svd(A)
    r = np.linalg.matrix_rank(A)
    S = np.diag(s)
    while True:
        k = int(input("Introduceti nivelul de trunchiere k= "))
        if k<=r:
            break
    uk = np.zeros((m, k))
    for i in range(m):
        for j in range(k):
            uk[i, j] = U[i, j]
    sk=np.zeros((k,k))
    for i in range(k):
        for j in range(k):
            sk[i, j] = S[i, j]
    x,y = Vt.shape
    vk = np.zeros((k, x))
    for i in range(k):
        for j in range(x):
            vk[i,j]=Vt[i,j]
    Ak = np.dot(np.dot(uk, sk), vk)
    q = np.zeros((m, 1))
    cerere = input("Cerere: ")
    cuvinte = cerere.split()
    for i in range(len(cuvinte)):
        for j in range(len(t)):
            if cuvinte[i] == t[j]:
                q[j] = 1
    print('q = ', q.T)
    cos = np.zeros((n, 1))
    for i in range(n):
        cos[i] = np.dot(q.T, Ak[:, i])/ (norm(q) * norm(A[:, i]))

    out= np.argsort(cos, axis=0)
    print(out)

dataSet(10)

import numpy as np
import os
from collections import Counter


def dictionary():
    return ["sport", "tennis", "gold", "champion", "record", "doping", "race", "Olympic", "football", "win", "lose",
            "athlete", "medals", "transfer", "world", "teams", "victory", "rules", "coach", "former", "performed",
            "championship", "athletics", "club", "qualification", "national", "international", "awards", "success",
            "season"]


def search_engine(n, k):
    d = dictionary()
    m = len(d)
    A = np.zeros((m, n))
    files = []
    directory = "E:/OneDrive - Universitatea „OVIDIUS”/Univ/Info3/Tehnici de optimizare/bbc_sport"
    j = 0
    df = np.zeros(m)
    dl = np.zeros(n)
    it = 0
    for file in os.listdir(directory):
        files.append(file)
        filepath = os.path.join(directory, file)
        f = open(filepath, 'r')
        dl[it] = os.stat(filepath).st_size
        it += 1
        wordcount = Counter(f.read().split())
        for i in range(m):
            nr = wordcount[d[i]]
            if nr != 0:
                df[i] += 1
            A[i, j] = nr
        f.close()
        j += 1
    W = np.zeros((m, n))  # weights matrix
    for i in range(m):
        idf = np.log(n / df[i])
        for j in range(n):
            tf = A[i][j] / max(A[i, :])
            W[i][j] = tf * idf

    U, s, Vt = np.linalg.svd(W)
    S = np.diag(s)

    uk = np.zeros((m, k))
    for i in range(m):
        for j in range(k):
            uk[i, j] = U[i, j]

    sk = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            sk[i, j] = S[i, j]

    x, y = Vt.shape
    vk = np.zeros((k, x))
    for i in range(k):
        for j in range(x):
            vk[i, j] = Vt[i, j]

    Wk = np.dot(np.dot(uk, sk), vk)
    return W, Wk, df, dl

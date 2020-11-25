import time as t
import numpy as np
import os
from collections import Counter
from numpy.linalg import norm


d = ["sport", "tennis", "gold", "champion", "record", "doping", "race", "Olympic", "football", "win", "lose", "athlete",
     "medals", "transfer", "world", "teams", "victory", "rules", "coach", "former", "performed", "championship",
     "athletics", "club", "qualification", "national", "international", "awards", "success", "season"]


def dataSet(n):
    dictionary = d
    m = len(dictionary)
    A = np.zeros((m, n))
    files = []
    directory = "../bbc_sport"
    j = 0
    df = np.zeros(m)
    for file in os.listdir(directory):
        files.append(file)
        filepath = os.path.join(directory, file)
        f = open(filepath, 'r')
        wordcount = Counter(f.read().split())
        for i in range(m):
            nr = wordcount[dictionary[i]]
            if nr != 0:
                df[i] += 1
            A[i, j] = nr
        f.close()
        j += 1

    W = np.zeros((m, n))  # weights matrix
    for i in range(m):
        idf = np.log(n / df[i])
        for j in range(n):
            tf = A[i][j]/max(A[i, :])
            W[i][j] = tf * idf

    U, s, Vt = np.linalg.svd(W)
    S = np.diag(s)
    r = np.linalg.matrix_rank(W)
    while True:
        k = int(input("Truncated level k= "))
        if k <= r:
            break

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
    q = np.zeros((m, 1))
    request = input("Request: ")
    words = request.split()
    nrr = np.zeros((m, 1))

    for i in range(len(words)):
        for j in range(len(dictionary)):
            if words[i] == dictionary[j]:
                nrr[j] += 1
    for i in range(len(words)):
        for j in range(len(dictionary)):
            if words[i] == dictionary[j]:
                wordcount = Counter(words)
                nr = wordcount[dictionary[j]]
                idf = np.log(n / df[j])
                tf = nr / max(nrr[j])
                q[j] = tf * idf

    cos = np.zeros((n, 1))

    t0 = t.perf_counter()
    for i in range(n):
        cos[i] = np.dot(q.T, Wk[:, i]) / norm(q) * norm(W[:, i])
    t1 = t.perf_counter()
    out = np.argsort(-1*cos, axis=0)[:n]
    tol = float(input("Tolerance tol= "))
    print("Returned in ", str(t1-t0))
    a = 0
    b = 0
    c = 0
    for i in range(n):
        j = out[i]
        if cos[j] > tol:
            print("Document ", j)
            a += 1
        if cos[j] > 0.5:
            b += 1
        if cos[j] > 0:
            c += 1

    precision = a / c
    print("Precision: ", precision)
    recall = a / b
    print("Recall: ", recall)


dataSet(40)

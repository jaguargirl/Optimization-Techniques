from numpy.linalg import norm
import numpy as np
from collections import Counter
import math
import time as t
import random


def calcRel(q, W, n, m):
    total = 0
    for j in range(n):
        nr = 0
        for i in range(m):
            if q[i]*W[i, j] != 0:
                nr += 1
        if nr != 0:
            total += 1
    return total


def calcCos(q, W, Wk, n):
    cos = np.zeros((n, 1))
    t0 = t.perf_counter()
    for i in range(n):
        cos[i] = np.dot(q.T, Wk[:, i]) / norm(q) * norm(W[:, i])
    t1 = t.perf_counter()
    out = np.argsort(-1*cos, axis=0)[:n]
    reTime = t1 - t0
    return cos, out, reTime


def calcOkapi(q, df, dl, m, W, n):
    avdl = np.mean(dl)
    k1 = random.uniform(1.2, 2)
    b = random.uniform(0.5, 0.8)
    okapi = np.zeros((n, 1))
    t0 = t.perf_counter()
    for j in range(n):
        summ = 0
        for i in range(m):
            r0 = math.log((n - df[i] + 0.5) / (df[i] + 0.5))
            r1 = ((k1 + 1) * W[i, j]) / ((k1 * (1 - b + b * (dl[j] / avdl)))+W[i, j])
            r2 = ((k1 + 1) * q[i]) / (k1 + q[i])
            summ += r0 * r1 * r2
        okapi[j] = summ
    t1 = t.perf_counter()
    okapi_out = np.argsort(-1 * okapi, axis=0)[:n]
    reTime = t1 - t0
    return okapi, okapi_out, reTime


def calcQ(d, request, df, n):
    m = len(d)
    q = np.zeros((m, 1))
    words = request.split()
    nrr = np.zeros((m, 1))
    for i in range(len(words)):
        for j in range(len(d)):
            if words[i] == d[j]:
                nrr[j] += 1
    for i in range(len(words)):
        for j in range(len(d)):
            if words[i] == d[j]:
                wordcount = Counter(words)
                nr = wordcount[d[j]]
                idf = np.log(n / df[j])
                tf = nr / max(nrr[j])
                q[j] = tf * idf
    return q

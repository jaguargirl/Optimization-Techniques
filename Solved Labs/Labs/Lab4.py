import numpy as np
import time as t

A = np.random.random((5, 5))
d, P = np.linalg.eig(A)
d = sorted(d, reverse=True)

print("d ", d)
print("P ", P)

D = np.diag(d)
print("D ", D)
print(np.dot(A, P)-np.dot(P, D))

t0 = t.perf_counter()
U, s, Vt = np.linalg.svd(A)
m, n = A.shape
sigmaplus = np.zeros((n, m)) #matrice ajutatoare
r = np.linalg.matrix_rank(A)

sigmaplus[: A.shape[1], : A.shape[1]] =  np.diag(1/s)
Aplus = np.dot(Vt.T, np.dot(sigmaplus, U.T))
t1 = t.perf_counter()
print(t1 - t0)

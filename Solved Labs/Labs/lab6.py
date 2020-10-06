import numpy as np
import time

A = np.random.random((5, 3))
m, n = A.shape
t0 = time.perf_counter()
U, s, Vt = np.linalg.svd(A)
S_plus = np.zeros((n, m))
r = np.linalg.matrix_rank(A)
S_plus[: A.shape[1], : A.shape[1]] = np.diag(1/s)

A_plus = np.dot(np.dot(Vt.T, S_plus), U.T)
print(A_plus)
t1 = time.perf_counter()
t2 = time.perf_counter()
A_pinv = np.linalg.pinv(A)
print(A_pinv)
t3 = time.perf_counter()
print(np.allclose(A_plus, A_pinv))
print(t1-t0)
print(t3-t2)

import numpy as np


def nonlin(x, deriv=False):
    if deriv:
        return x*(1-x)
    return 1/(1+np.exp(-x))


X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])
y = np.array([[0],
              [1],
              [1],
              [0]])
np.random.seed(1)
# initializare ponderi
W0 = 2*np.random.random((3, 4)) - 1
W1 = 2*np.random.random((4, 1)) - 1
for j in range(60000):
    # propagare inainte pt layers 0, 1 si 2
    l0 = X
    l1 = nonlin(np.dot(l0, W0))
    l2 = nonlin(np.dot(l1, W1))
    # evaluam eroarea dupa o trecere
    l2_error = y - l2
    if (j % 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))
    l2_delta = l2_error*nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(W1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True)
    # actualizam ponderile cu metoda gradient descent
    W1 += l1.T.dot(l2_delta)
    W0 += l0.T.dot(l1_delta)
print(l2)

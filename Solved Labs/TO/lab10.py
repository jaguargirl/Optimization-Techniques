import numpy as np
from sklearn import datasets
from sklearn.preprocessing import LabelBinarizer


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def softmax(a):
    expA = np.exp(a)
    return expA/expA.sum(axis=1, keepdims=True)


def forward(x, w1, w2):
    z = sigmoid(x.dot(w1))
    y = softmax(z.dot(w2))
    return y, z


def derivative_w2(z, t, y):
    return (z.T).dot(y-t)


def derivative_w1(x, z, t, y, w2):
    dz = (y - t).dot(w2.T) * z * (1 - z)
    return x.T.dot(dz)


def nonlin(x, deriv=False):
    if deriv:
        return x*(1-x)
    return 1/(1+np.exp(-x))


def optimize(algorithm, v1, v2, w1, w2):
    if algorithm == 'momentum':
        v2 = mu * v2 - learning_rate * derivative_w2(hidden, T, output)
        w2 = w2 + v2
        v1 = mu * v1 - learning_rate * derivative_w1(X, hidden, T, output, w2)
        w1 = w1 + v1
    elif algorithm == 'descent':
        w2 -= learning_rate * derivative_w2(hidden, T, output)
        w1 -= learning_rate * derivative_w1(X, hidden, T, output, w2)
    elif algorithm == 'nesterov':
        v_prev2 = v2
        v2 = mu * v2 - learning_rate * derivative_w2(hidden, T, output)
        w2 = w2 - mu * v_prev2 + (1 + mu) * v2
        v_prev1 = v1
        v1 = mu * v1 - learning_rate * derivative_w1(X, hidden, T, output, w2)
        w1 = w1 - mu * v_prev1 + (1 + mu) * v1
    return v1, v2, w1, w2


d = 4
m = 5
k = 3

w1 = np.random.randn(d, m) - 0.5
w2 = np.random.randn(m, k) - 0.5
v1 = np.zeros((d, m))
v2 = np.zeros((m, k))
m1 = np.zeros((d, m))
m2 = np.zeros((m, k))

lb = LabelBinarizer()
lb.fit([0, 1, 2])
iris = datasets.load_iris()
iris_one_hot = lb.transform([t for t in iris.target])
X = iris.data / iris.data.max(axis=0)
T = iris_one_hot

eps = 10e-8
beta1 = 0.9
beta2 = 0.999

mu = 0.9
learning_rate = 0.01
output, hidden = forward(X, w1, w2)

algorithm = input('Introduceti algoritmul: ')

for j in range(60000):
    # propagare inainte pt layers 0, 1 si 2
    l0 = X
    l1 = nonlin(np.dot(l0, w1))
    l2 = nonlin(np.dot(l1, w2))
    # evaluam eroarea dupa o trecere
    l2_error = T - l2
    if (j % 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))
    l2_delta = l2_error*nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(w2.T)
    l1_delta = l1_error * nonlin(l1, deriv=True)
    #actualizam ponderile cu metoda gradient descent
    v1, v2, w1, w2 = optimize(algorithm, v1, v2, w1, w2)
print(l2)





import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('date.csv')
t = dataset['x1'].values.reshape(-1, 1)
b = dataset['Y2_normalizat'].values.reshape(-1, 1)
m = len(t)

A = np.ones((m, 1))
A = np.hstack((A, t))
x = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, b))
t1 = np.linspace(min(t), max(t), 20)
x = x[::-1]
y = np.polyval(x, t1)

plt.plot(t, b, "ro")
plt.plot(t1, y)
plt.xlabel("t")
plt.ylabel("b")
plt.title("Regresie liniara univariata")
plt.legend(["Datele noastre", "Dreapta de regresie"])
plt.show()
er1 = np.dot(A, x)
er2 = np.linalg.norm((er1 - b))
erf = np.dot(er2,er2)
print('Eroare: ', erf)

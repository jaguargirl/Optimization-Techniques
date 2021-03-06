import numpy as np
import matplotlib.pyplot as plt

m = int(input("Introduce m= "))
t = np.random.random((m, 1))
b = np.random.random((m, 1))
A = np.ones((m, 1))
A = np.hstack((A, t))

x = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, b))

t1 = np.linspace(min(t), max(t), 20)
err = np.linalg.norm(np.dot(A, x)-b)**2
print("Error: ",err)

x = x[::-1]
y = np.polyval(x, t1)

plt.plot(t, b, "ro")
plt.plot(t1, y)
plt.xlabel("t")
plt.ylabel("b")
plt.title("Univariate liniar regression")
plt.legend(["Our data", "Regression line"])
plt.show()


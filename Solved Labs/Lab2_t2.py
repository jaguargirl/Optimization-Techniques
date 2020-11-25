import numpy as np
import matplotlib.pyplot as plt

m = int(input("Introduce m="))
b = np.random.random((m, 1))
t = np.random.random(m)
n = m-1
A = np.vander(t, n, increasing=True)
print(A)
x = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, b))
u = np.linspace(min(t), max(t), 20)
err = np.linalg.norm(np.dot(A, x)-b)**2
print("Eroare: ", err)

x = x[::-1]
y = np.polyval(x, u)

plt.plot(t, b, "ro")
plt.plot(u, y)
plt.xlabel("t")
plt.ylabel("b")
plt.title("Liniar regression")
plt.legend(["Our data", "Regression curbe"])
plt.show()

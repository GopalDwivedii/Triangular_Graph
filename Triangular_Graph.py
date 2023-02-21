import numpy as np
import matplotlib.pyplot as plt

a = (10, 20, 30, 90, 100, 43, 1)
b = (1, 2, 3)
c = np.random.triangular(4, 4, 8, 2500)
d = np.random.triangular(2, 2, 4, 2000)
e = np.random.triangular(1, 2, 3, 5000)

plt.xlabel("Height")
plt.ylabel("Width")
plt.title("Graph ploting Sample")
plt.hist(c, color="blue")
plt.hist(e, color="orange")
plt.hist(d, color="lightgreen")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = x[::-1]
X, Y = np.meshgrid(x, y)

U = -Y
V = X

plt.quiver(x, y, U, V)

plt.savefig("Plots/quiver_plot.png")
plt.clf()

x = np.linspace(1, 10, 20)
y = np.linspace(1, 10, 20)
X, Y = np.meshgrid(x, y)

U = np.sin(X) * np.cos(Y)
V = np.cos(X) * np.sin(Y)

plt.quiver(X, Y, U, V, color='r')

plt.savefig("Plots/quiver_plot_meshgrid.png")
plt.clf()
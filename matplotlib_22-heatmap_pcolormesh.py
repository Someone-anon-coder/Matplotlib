import matplotlib.pyplot as plt
import numpy as np

x = [1, 4, 13, 19, 32]
y = [45, 69, 71, 72, 99]

z = [
    [6, 7, 8, 9, 10], 
    [16, 17, 18, 19, 20],
    [1, 2, 3, 4, 5], 
    [21, 22, 23, 24, 25],
    [11, 12, 13, 14, 15]
]

plt.pcolormesh(x, y, z, cmap='plasma')

plt.savefig("Plots/fig_with_pcolormesh.png")
plt.clf()

x = np.arange(0, 5, 1)
y = np.arange(0, 5, 1)

z = np.random.rand(5, 5)

plt.pcolormesh(x, y, z, cmap='viridis', shading='auto', edgecolor='black', linewidth=1, antialiased=True)

plt.savefig("Plots/fig_with_pcolormesh_custom.png")
plt.clf()
import matplotlib.pyplot as plt
import numpy as np

x = [
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10], 
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

plt.imshow(x, cmap='hot')

plt.savefig("Plots/fig_with_heatmap.png")
plt.clf()

x = np.random.rand(5, 5)

plt.imshow(x, cmap='coolwarm', interpolation='none', aspect='auto')

plt.savefig("Plots/fig_with_heatmap_custom.png")
plt.clf()
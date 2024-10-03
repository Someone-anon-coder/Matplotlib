import matplotlib.pyplot as plt
import numpy as np

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7]

plt.hist(data, bins=7)

plt.savefig("Plots/fig_with_histogram.png")
plt.clf()

data = np.random.randn(1000)

plt.hist(data, bins=30, color='green', edgecolor='black', density=True, cumulative=True)

plt.savefig("Plots/fig_with_histogram_color.png")
plt.clf()
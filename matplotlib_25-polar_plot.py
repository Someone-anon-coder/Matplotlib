import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = np.linspace(0, 5, 10)

fig = plt.figure()

ax = fig.add_subplot(111, polar=True)
ax.plot(x, y)

plt.savefig("Plots/fig_with_polar_plot.png")
plt.clf()

theta = np.linspace(0, 2 * np.pi, 100)
radius = np.abs(np.sin(2 * theta))

fig = plt.figure()

ax = fig.add_subplot(111, polar=True)
ax.plot(theta, radius, color='b', linestyle='--', linewidth=2)

plt.savefig("Plots/fig_with_polar_plot_custom.png")
plt.clf()
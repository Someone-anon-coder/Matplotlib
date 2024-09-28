import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.plot(x, y)
plt.xlim([2, 4])
plt.ylim([2, 4])

plt.savefig("Plots/fig_with_xlim_ylim.png")

plt.xlim([5, 2])
plt.ylim([2, 5])

plt.savefig("Plots/fig_with_xlim_ylim_reversed.png")

plt.autoscale(False)
plt.xlim([2, 4])
plt.ylim([5, 2])
plt.savefig("Plots/fig_with_no_autoscale.png")

plt.autoscale(True, axis='x')

x = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

plt.plot(x, y)
plt.gca().set_aspect('equal')
plt.savefig("Plots/fig_with_equal_aspect_tight_layout.png")
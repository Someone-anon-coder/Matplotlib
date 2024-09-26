import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.plot(x, y, marker="o")

plt.plot(x, [y_i-1 for y_i in y], marker="x")
plt.plot(x, [y_i-3 for y_i in y], marker="^")

plt.plot(x, [y_i+1 for y_i in y], marker="s", markersize=10, markerfacecolor="red", markeredgecolor="blue")

plt.savefig("Plots/fig_with_markers.png")
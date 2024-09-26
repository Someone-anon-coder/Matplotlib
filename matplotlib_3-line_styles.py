import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.plot(x, y, linestyle="-")

plt.plot(x, [y_i-1 for y_i in y], linestyle="--")
plt.plot(x, [y_i-2 for y_i in y], linestyle="-.")
plt.plot(x, [y_i-3 for y_i in y], linestyle=":")

plt.savefig("Plots/fig_with_linestyles.png")
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.plot(x, y, color="blue")

plt.plot(x, [y_i-1 for y_i in y], color="r")
plt.plot(x, [y_i-2 for y_i in y], color="#FF5733")
plt.plot(x, [y_i-3 for y_i in y], color=(0, 1, 0))

plt.savefig("Plots/fig_with_colors.png")
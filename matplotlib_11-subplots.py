import matplotlib.pyplot as plt

x = [1, 2, 3]
y1 = [1, 4, 9]
y2 = [1, 2, 3]
y3 = [2, 3, 4]
y4 = [3, 5, 7]

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(x, y1)
ax[0, 0].set_title("Plot 1")

ax[0, 1].plot(x, y2)
ax[0, 1].set_title("Plot 2")

ax[1, 0].plot(x, y3)
ax[1, 0].set_title("Plot 3")

ax[1, 1].plot(x, y4)
ax[1, 1].set_title("Plot 4")

plt.tight_layout()
plt.savefig("Plots/fig_with_multiple_subplots_title.png")
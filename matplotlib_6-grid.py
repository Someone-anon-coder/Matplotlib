import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.plot(x, y)
# plt.grid(True)
# plt.savefig("Plots/fig_with_grid.png")

# plt.grid(True, axis='x')
# plt.savefig("Plots/fig_with_grid_x.png")

# plt.grid(True, axis='y')
# plt.savefig("Plots/fig_with_grid_y.png")

plt.grid(True, axis='both', linestyle='--', color='red', alpha=0.5)
plt.savefig("Plots/fig_with_grid_both_dashed_red.png")
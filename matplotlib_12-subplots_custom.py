import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(8, 6))

ax[0, 0].plot([1, 2, 3], [1, 4, 9])
ax[0, 0].set_title("Plot 1")

ax[0, 1].plot([1, 2, 3], [1, 2, 3])
ax[0, 1].set_title("Plot 2")

ax[1, 0].plot([1, 2, 3], [2, 3, 4])
ax[1, 0].set_title("Plot 3")

ax[1, 1].plot([1, 2, 3], [3, 5, 7])
ax[1, 1].set_title("Plot 4")

plt.tight_layout()
plt.savefig("Plots/fig_with_multiple_custom_subplots.png")
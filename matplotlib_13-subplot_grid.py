import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [i*i for i in x]
y2 = [i*i*i for i in x]
y3 = x[::-1]
y4 = [0, 0, 1, 2, 3, 5, 8, 13, 21, 34]

fig = plt.figure(figsize=(8, 6))
gs = gridspec.GridSpec(3, 3)

ax1 = fig.add_subplot(gs[0, 0:2])
ax2 = fig.add_subplot(gs[0, 2])
ax3 = fig.add_subplot(gs[1, :])
ax4 = fig.add_subplot(gs[2, 0:3])

ax1.plot(x, y1, label = "y = x^2")
ax2.plot(x, y2, label = "y = x^3")
ax3.plot(x, y3, label = "y = reverse(x)")
ax4.plot(x, y4, label = "y = fibbonacci place")

fig.tight_layout()
fig.savefig("Plots/fig_with_multiple_plots_gridspec.png")
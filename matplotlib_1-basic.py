import matplotlib.pyplot as plt

x_axis = [1, 2, 3, 4]
y_axis = [4, 3, 2, 1]

fig, ax = plt.subplots()
ax.plot(x_axis, y_axis)
fig.savefig("Plots/basic_plot.png")
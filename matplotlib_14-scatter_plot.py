import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [i*i for i in x]
y2 = [i*i*i for i in x]
y3 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

plt.scatter(x, y1, s=100, c='blue', marker='o', alpha=0.7)
plt.scatter(x, y2, s=100, c='green', marker='x', alpha=0.7)
plt.scatter(x, y3, s=100, c='red', marker='s', alpha=0.7)

plt.savefig("Plots/scatter_plot.png")
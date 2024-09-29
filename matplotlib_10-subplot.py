import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [i*i for i in x]
y2 = [i*i*i for i in x]
y3 = x[::-1]
y4 = [0, 0, 1, 2, 3, 5, 8, 13, 21, 34]

plt.subplot(2, 2, 1)
plt.plot(x, y1, label = "y = x^2", linestyle = '--', color = 'blue')
plt.title("Plot 1")

plt.subplot(2, 2, 2)
plt.plot(x, y2, label = "y = x^3", linestyle = '-', color = 'green')
plt.title("Plot 2")

plt.subplot(2, 2, 3)
plt.plot(x, y3, label = "y = reverse(x)", linestyle = ':', color = 'red')
plt.title("Plot 3")

plt.subplot(2, 2, 4)
plt.plot(x, y4, label = "y = fibbonacci place(x)", linestyle = '-.', color = 'orange')
plt.title("Plot 4")

plt.tight_layout()
plt.savefig("Plots/fig_with_multiple_plots.png")
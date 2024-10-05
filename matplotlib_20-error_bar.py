import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5.1, 4.2, 2.9, 1.8, 1.1]
yerr = [0.1, 0.2, 0.1, 0.2, 0.1]

plt.errorbar(x, y, yerr=yerr)

plt.savefig("Plots/fig_with_errorbar.png")
plt.clf()

x = [0.9, 1.8, 2.7, 3.6, 4.5, 5.5, 6.6, 7.7, 8.8, 9.9]
xerr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.2, 0.1]

y = [1.1, 2.2, 3.3, 4.4, 5.5, 6.5, 7.4, 8.3, 9.2, 10.1]
yerr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.2, 0.1]

plt.errorbar(x, y, yerr=yerr, xerr=xerr, fmt='o', ecolor='red', capsize=5, elinewidth=2)

plt.savefig("Plots/fig_with_errorbar_custom.png")
plt.clf()
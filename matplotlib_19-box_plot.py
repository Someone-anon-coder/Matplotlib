import matplotlib.pyplot as plt

data = [1, 2, 19, 20, 21, 39, 40, 77]

plt.boxplot(data)

plt.savefig("Plots/fig_with_boxplot.png")
plt.clf()

new_data = [26, 61, 62, 79, 80, 81, 99, 100]

plt.boxplot(new_data, vert=False, patch_artist=True, notch=True, showmeans=True)

plt.savefig("Plots/fig_with_boxplot_custom.png")
plt.clf()
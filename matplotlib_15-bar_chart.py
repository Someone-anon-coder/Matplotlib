import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 15, 8, 20]

plt.bar(categories, values)
plt.savefig("Plots/bar_chart.png")

x = ['ABC', 'PQR', 'DEF', 'XYZ']
height = [10, 7, 17, 13]

plt.bar(x, height=height, width=0.5, color='green')
plt.savefig("Plots/bar_plot_width_color.png")
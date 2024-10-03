import matplotlib.pyplot as plt

y = ["A", "B", "C", "D"]
width = [10, 7, 17, 13]

plt.barh(y, width)
plt.savefig("Plots/bar_horizontal_chart.png")

categories = ["ABC", "PQR", "DEF", "XYZ"]
values = [22, 17, 5, 12]

plt.barh(categories, values, height=0.5, color='green', alpha=0.7)
plt.savefig("Plots/bar_horizontal_chart_width_color.png")
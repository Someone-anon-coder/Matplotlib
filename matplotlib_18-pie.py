import matplotlib.pyplot as plt

sizes = [15, 30, 45, 20]
labels = ["A", "B", "C", "D"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.axis('equal')

plt.savefig("Plots/pie_chart.png")
plt.clf()

sizes = [10, 5, 15, 45, 25]
labels = ["Ten", "Five", "Fifteen", "Forty Five", "Twenty Five"]
colors = ["red", "green", "orange", "blue", "yellow"]

plt.pie(sizes, explode=(0, 0.2, 0, 0, 0), labels=labels, colors=colors, autopct="%1.1f%%", startangle=90, shadow=True)
plt.axis('equal')

plt.savefig("Plots/pie_chart_custom.png")
plt.clf()
import matplotlib.pyplot as plt

x = [i for i in range(1, 11)]
y = x[::-1]

plt.plot(x, y)

plt.xticks([2, 6, 10])
plt.yticks([1, 5, 9])
plt.savefig("Plots/fig_with_number_ticks.png")

plt.xticks([2, 6, 10], labels=["Two", "Six", "Ten"])
plt.yticks([1, 5, 9], labels=["One", "Five", "Nine"])
plt.savefig("Plots/fig_with_string_ticks.png")

plt.xticks([2, 6, 10], labels=["Two", "Six", "Ten"], rotation=45)
plt.yticks([1, 5, 9], labels=["One", "Five", "Nine"], rotation=-45)
plt.savefig("Plots/fig_with_rotated_ticks.png")

plt.xticks([1, 3, 5, 7, 9], labels=["One", "Three", "Five", "Seven", "Nine"], fontsize=10, color="red", rotation=0)
plt.yticks([10, 8, 6, 4, 2], labels=["Ten", "Eight", "Six", "Four", "Two"], fontsize=10, color="green", rotation=0)
plt.savefig("Plots/fig_with_font_color_ticks.png")
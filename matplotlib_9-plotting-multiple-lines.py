import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [i*i for i in x]
y2 = [i*i*i for i in x]
y3 = x[::-1]

plt.plot(x, y1, label="y = x^2", linestyle='--', color='blue')
plt.plot(x, y2, label="y = x^3", linestyle='-', color='green')
plt.plot(x, y3, label="y = reverse(x)", linestyle=':', color='red')

plt.savefig("Plots/fig_with_multiple_lines.png")
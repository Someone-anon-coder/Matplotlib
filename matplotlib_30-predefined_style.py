import matplotlib.pyplot as plt
import numpy as np

print(plt.style.available)

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.style.use('ggplot')

plt.plot(x, y1, label='Sine Wave', color='blue', linestyle='--', linewidth=2)
plt.plot(x, y2, label='Cosine Wave', color='green', linestyle='-', linewidth=2)

plt.savefig("Plots/fig_with_style_ggplot.png")
plt.clf()

plt.style.use('classic')

plt.plot(x, y1, label='Sine Wave', color='blue', linestyle='--', linewidth=2)
plt.plot(x, y2, label='Cosine Wave', color='green', linestyle='-', linewidth=2)

plt.savefig("Plots/fig_with_style_classic.png")
plt.clf()

plt.style.use('dark_background')

plt.plot(x, y1, label='Sine Wave', color='blue', linestyle='--', linewidth=2)
plt.plot(x, y2, label='Cosine Wave', color='green', linestyle='-', linewidth=2)

plt.savefig("Plots/fig_with_style_dark-background.png")
plt.clf()

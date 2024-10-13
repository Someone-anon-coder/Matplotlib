import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
line1, = plt.plot(x, y1, label='Sine Wave', color='blue', linestyle='--', linewidth=2)
line2, = plt.plot(x, y2, label='Cosine Wave', color='green', linestyle='-', linewidth=2)

plt.legend(loc='upper right', fontsize=12, title='Legend Title', title_fontsize='13', shadow=True)
plt.tight_layout()

plt.savefig("Plots/fig_with_legend.png")
plt.clf()
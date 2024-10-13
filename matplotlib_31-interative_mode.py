import matplotlib.pyplot as plt
import numpy as np

plt.ion()

x = np.linspace(0, 10, 100)
for i in range(1, 4):
    plt.plot(x, np.sin(i * x))
    plt.title(f'Interactive Plot - Wave {i}')

    plt.pause(1)
    plt.savefig(f'Plots/interactive_plot_{i}.png')

    plt.clf()
plt.ioff()
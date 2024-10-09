import matplotlib.pyplot as plt
import numpy as np

x = np.logspace(0, 3, 100)
y = np.sqrt(x)

plt.semilogx(x, y, marker='s', markersize=5)

plt.savefig("Plots/fig_with_semilogx.png")
plt.clf()

x = np.linspace(0, 10, 50)
y = np.exp(x)

plt.semilogy(x, y, marker='o', markersize=5)

plt.savefig("Plots/fig_with_semilogy.png")
plt.clf()

x = np.logspace(0, 5, 100)
y = np.logspace(0, 3, 100)

plt.loglog(x, y, marker='x', markersize=5, linestyle='--', color='red')

plt.savefig("Plots/fig_with_loglog.png")
plt.clf()
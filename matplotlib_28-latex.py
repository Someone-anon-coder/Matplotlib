import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.text(np.pi, y[int(len(y)/2) - 1], r'$\sin(x)$')

plt.savefig('Plots/fig_with_latex.png')
plt.clf()

plt.plot(x, y)

plt.text(1, 0.50, r'$E = mc^2$')
plt.text(1, 0, r'$\frac{d}{dx}e^x = e^x$')
plt.text(4, 0.50, r'$\sum_{i=1}^n i = \frac{n(n + 1)}{2}$')
plt.text(4, 0, r'$\int_0^\infty e^{-x^2}dx = \frac{\sqrt{\pi}}{2}$')

plt.savefig('Plots/fig_with_latex_text.png')
plt.clf()
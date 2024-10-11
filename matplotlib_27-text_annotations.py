import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)

plt.text(
    x[int(len(x)/2) - 1], 
    y[int(len(y)/2) - 1], 
    "Sine Wave", 
    fontsize=12, 
    color='red', 
    fontweight='bold', 
    bbox = {
        'facecolor': 'yellow', 
        'alpha': 0.5, 
        'pad': 5
    }
)

plt.savefig("Plots/fig_with_text.png")
plt.clf()

plt.figure(figsize=(10, 6))
plt.plot(x, y)

plt.annotate(
    'Maximum Point', 
    xy=(np.pi/2, 1), 
    xytext=(np.pi/2 + 0.5, 0.8), 
    arrowprops=dict(
        facecolor='black', 
        shrink=0.05, width=2
    ),
    fontsize=12, 
    color='green'
)

plt.annotate(
    'Minimum Point', 
    xy=(np.pi + np.pi/2, -1), 
    xytext=(np.pi + 0.5, -0.8), 
    arrowprops=dict(
        facecolor='black', 
        shrink=0.05, 
        width=2
    ), 
    fontsize=12, 
    color='blue'
)

plt.savefig("Plots/fig_with_annotation.png")
plt.clf()
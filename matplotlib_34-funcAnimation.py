import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
line, = plt.plot([], [], 'ro-', animated=True)

def init():
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)
    return line,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    line.set_data(xdata, ydata)
    return line,

ani = FuncAnimation(
    fig, 
    update, 
    frames=np.linspace(0, 2 * np.pi, 128),
    init_func=init, blit=True
)

plt.show()
plt.clf()
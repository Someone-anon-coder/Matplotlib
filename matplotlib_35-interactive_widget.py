import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)

x = np.linspace(0, 2 * np.pi, 1000)
initial_frequency = 1

y = np.sin(initial_frequency * x)
line, = plt.plot(x, y, lw=2)

ax_slider = plt.axes([0.1, 0.1, 0.65, 0.03])
frequency_slider = Slider(ax_slider, 'Frequency', 0.1, 5.0, valinit=initial_frequency)

def update(val):
    frequency = frequency_slider.val
    line.set_ydata(np.sin(frequency * x))
    fig.canvas.draw_idle()

frequency_slider.on_changed(update)

plt.show()
plt.clf()
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.savefig("Plots/Empty_fig_no_graph.png")

fig, ax = plt.subplots()
fig.savefig("Plots/fig_with_single_graph.png")

fig, ax = plt.subplots(2)
fig.savefig("Plots/fig_with_two_graph.png")

fig, ax = plt.subplots(1, 2)
fig.savefig("Plots/fig_with_two_vertical_graph.png")

fig, ax = plt.subplots(2, 1)
fig.savefig("Plots/fig_with_two_horizontal_graph.png")

fig, ax = plt.subplots(2, 2)
fig.savefig("Plots/fig_with_two_by_two_graph.png")

fig, ax = plt.subplot_mosaic([["left", "right-top"], ["left", "right-bottom"]])
fig.savefig("Plots/fig_with_one_left_two_right_graph.png")

x1 = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x1)

x2 = np.linspace(0, 2 * np.pi, 100)
y2 = np.cos(x2)

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(x1, y1)
ax2.plot(x2, y2)

fig.savefig("Plots/fig_with_sine_cosine_graph.png")
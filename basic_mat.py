import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(0, 2 * numpy.pi, 200)
y = numpy.sin(x)
print(y)

plt.plot(x,y)
plt.savefig("Plots/basic_sin_plot.png")
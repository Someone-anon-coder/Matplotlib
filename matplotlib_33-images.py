import matplotlib.pyplot as plt
import numpy as np

image_data = np.random.rand(10, 10)

plt.imshow(image_data, cmap='viridis')

plt.savefig("Plots/fig_with_image.png")
plt.clf()

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)

X, Y = np.meshgrid(x, y)

Z = np.sin(X**2 + Y**2)

plt.imshow(Z, extent=[-3, 3, -3, 3], origin='lower', cmap='coolwarm')

plt.savefig("Plots/fig_with_image_meshgrid.png")
plt.clf()

data = np.random.rand(10, 10)
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

ax[0].imshow(data, cmap='gray')
ax[0].set_title('Gray Colormap')

ax[1].imshow(data, cmap='hot')
ax[1].set_title('Hot Colormap')

ax[2].imshow(data, cmap='coolwarm')
ax[2].set_title('Coolwarm Colormap')

plt.savefig("Plots/fig_with_image_subplots.png")
plt.clf()
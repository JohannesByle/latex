import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin, pi
from matplotlib.cm import get_cmap


def cross_section(theta):
    return (cos(theta / 2) / sin(theta)) * abs((1 / 2) * sin(theta / 2))


def polar_to_cartesian(r, theta):
    return r * cos(theta), r * sin(theta)


thetas = np.linspace(10 ** -10, pi, 100)
print(thetas)
x, y = polar_to_cartesian(1, thetas)
colors = cross_section(thetas)
print(colors)
plt.plot(thetas, colors)
plt.show()
exit()
cm = get_cmap()
colors = [cm(n / max(colors)) for n in colors]
plt.scatter(x, y, c=colors)
plt.show()

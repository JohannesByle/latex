import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap, ScalarMappable
from matplotlib.colors import Normalize


def f(x_, x0=1, g=10):
    return (x_ ** 2) / 2 - (x0 * np.sqrt(1 + g * (x_ ** 2))) / (np.sqrt(1 + g * (x0 ** 2)))


def f_g(g_):
    return int(np.exp(g_) - 1)


cm = get_cmap()
num_g = 10

for g in range(num_g):
    color = cm(g / num_g)
    x = np.linspace(-3, 3, 1000)
    plt.plot(x, f(x, g=f_g(g)), color=color, label=f"g={f_g(g)}")
# plt.colorbar(ScalarMappable(norm=Normalize(vmin=0, vmax=f_g(num_g))), label="g")
plt.xlabel("x")
plt.ylabel("V")
plt.legend()
plt.savefig("potential_plot.png", dpi=200)
plt.show()

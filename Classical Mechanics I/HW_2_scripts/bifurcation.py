import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['text.usetex'] = True
from math import pi, sin
from tqdm import tqdm


def f(x_, mu_=0.5):
    return mu_ * sin(pi * x_)


def f2(x_, a=0.5):
    if x_ < 0.5:
        return 2 * a * x_
    else:
        return 2 * a * (1 - x_)


num_points = 1000
mu_array = []
x_array = []
for mu in tqdm(np.linspace(0, 1, num_points * 10)):
    x0 = 10 ** (-5)
    x = [x0]
    for _ in range(num_points):
        x0 = f(x0, mu_=mu)
        x.append(x0)
    final_slice = int(num_points / 100)
    mu_array += [mu] * final_slice
    x_array += x[-final_slice:]
plt.scatter(mu_array, x_array, c="black", s=0.1)
plt.ylabel("x")
plt.xlabel(r"$\mu$")
plt.savefig("bifurcation.png", dpi=500)
plt.show()

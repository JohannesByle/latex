import numpy as np
from scipy.optimize import minimize_scalar, root_scalar
import matplotlib.pyplot as plt
from numpy import sin, cos, pi
from tqdm import tqdm


def f(x_, mu_=0.5):
    return mu_ * sin(pi * x_)


def d_f(x_, mu_=0.5):
    return pi * mu_ * cos(pi * x_)


def d_d_f(x_, mu_=0.5):
    return -pi ** 2 * mu_ * sin(pi * x_)


x = np.linspace(0, 1, 100)
roots = []
derivatives = []
mu_s = []
diffs = []
num_points = 1000
final_slice = int(num_points / 100)
x0 = 0.1
for mu in tqdm(np.linspace(0, 1, 1000)):
    try:
        sol = root_scalar(lambda i: f(i, mu) - i, bracket=[0.1, 1])
        bifurcation_x = []
        for _ in range(num_points):
            x0 = f(x0, mu_=mu)
            bifurcation_x.append(x0)
        plt.scatter([mu] * final_slice, bifurcation_x[-final_slice:], alpha=0.5, color="black", s=0.5)
        diffs.append(sol.root - f(sol.root, mu_=mu))
        roots.append(sol.root)
        derivatives.append(d_f(sol.root, mu_=mu))
        mu_s.append(mu)
    except ValueError:
        pass
derivatives = np.array(derivatives)
d_root_1 = mu_s[np.abs(derivatives + 1).argmin()]
plt.plot(mu_s, roots, label="Roots")
plt.plot(mu_s, derivatives, label="Derivatives")
plt.vlines(d_root_1, min(derivatives), max(derivatives), color="black", label=r"$\frac{df}{dx}=-1$")
plt.xlabel(r"$\mu$")
plt.axis("on")
plt.legend()
plt.savefig("stability_bifurcation.png", dpi=200)
plt.show()

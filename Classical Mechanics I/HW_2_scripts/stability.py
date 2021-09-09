import numpy as np
from scipy.optimize import minimize_scalar, root_scalar
import matplotlib.pyplot as plt
from numpy import sin, cos, pi


def f(x_, mu_=0.5):
    return mu_ * sin(pi * x_)


def df(x_, mu_=0.5):
    return pi * mu_ * cos(pi * x_)


x = np.linspace(0, 1, 100)
roots = []
derivatives = []
mu_s = []
for mu in np.linspace(1 / pi, 1, 1000):
    try:
        # sol = root_scalar(lambda i: f(i, mu) - i, bracket=[0.1, 1])
        roots.append(1 / pi)
        derivatives.append(df(1 / pi, mu))
        mu_s.append(mu)
    except ValueError:
        pass

plt.plot(mu_s, roots, label="Roots")
plt.plot(mu_s, derivatives, label="Derivatives")
plt.legend()
plt.show()

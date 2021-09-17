import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos

t = np.linspace(0, 100, 1000)


def x(t_, c1_, c2_):
    return c1_ * sin(t_) + c2_ * cos(t_)


def x_dot(t_, c1_, c2_):
    return c1_ * cos(t_) - c2_ * sin(t_)


max_ = 10
for _ in range(7):
    c1, c2 = np.random.randint(0, max_), np.random.randint(0, max_)
    plt.scatter(x(t, c1, c2), x_dot(t, c1, c2), label=f"$c_1={c1}, c_2={c2}$")

plt.legend()
plt.xlabel("$x(t)$")
plt.ylabel(r"$\dot{x}(t)$")
plt.show()

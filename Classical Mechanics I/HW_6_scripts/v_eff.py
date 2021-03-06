import numpy as np
import matplotlib.pyplot as plt


def v(r_, l_=1.0, mu_=1.0, c_=1.0, a_=1.0):
    return (l_ ** 2) / (2 * mu_ * r_ ** 2) - c_ * (np.exp(-a_ * r_) / r_)


L = 0.6
mu = 0.5
c = 10
a = 10
r = np.linspace(10 ** -3, 1, 10 ** 4)
for L in np.linspace(0.6, .8, 3):
    L = round(L, 2)
    plt.plot(r, v(r, l_=L, mu_=mu, c_=c, a_=a), label=fr"$L={L},\ \mu={mu},\ c={c},\ a={a}$")
plt.ylim([-2, 10])
plt.xlabel(r"$r$")
plt.ylabel(r"$V_{eff}(r)$")
plt.legend()
plt.savefig("v_eff.png", dpi=300)
plt.show()

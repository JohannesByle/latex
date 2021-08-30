import numpy as np
import matplotlib.pyplot as plt
from collections.abc import Iterable
from scipy.integrate import quad

# t = np.linspace(-2, 10, 10000)
# v = np.zeros(np.shape(t))
# v[(t < 1) & (0 < t)] = 40
# r = np.zeros(np.shape(t))
# r[(t <= 1) & (0 < t)] = 100
# r[t > 1] = 200
# L = 200
#
#
# def integral(time):
#     def f(x):
#         if x < 0:
#             V = 0
#             R = 0
#         elif 0 <= x < 1:
#             V = 40
#             R = 100
#         else:
#             V = 0
#             R = 200
#         return (np.exp((R * x) / L) * V) / L
#
#     y, err = quad(f, 1, time)
#     return y
#
#
# f = np.array([integral(n) for n in t])
# i = np.exp(-(r * t) / L) * (f - f[0])
# plt.plot(t, i)
# plt.plot(t, i * 50)
# plt.show()

C = 0.001
L = 0.1
R_1 = (100 * L) / 0.1
R_2 = (100 * L) / 1
R_3 = (100 * L) / 10


def z(w, R):
    val = R + 1 / (1j * w * C) + 1j * w * L
    return (10 / np.sqrt(np.real(val * np.conj(val)))) / (np.sqrt(2))


w = np.linspace(10 ** (-2), 10 ** 6, 1000000)
plt.plot(w, z(w, R_1), label="Q=0.1")
plt.plot(w, z(w, R_2), label="Q=1")
plt.plot(w, z(w, R_3), label="Q=10")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Current (A)")
plt.xscale("log")
# plt.yscale("log")
plt.legend()
plt.show()

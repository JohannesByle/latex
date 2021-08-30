import numpy as np
import matplotlib.pyplot as plt


# R_1 = 52.7
# # R_1 = 1000
# R_2 = 1000
# R_2 = R_1
# C_1 = 10 ** (-3)
# C_2 = 10 ** (-3)
#
#
# def v(hz):
#     freq = 2 * np.pi * hz
#     z_tot = R_1 + (1j * freq * C_1 + (1 / (R_2 + (1 / (freq * C_2 * 1j))))) ** (-1)
#     numerator = (1 - (R_1 / z_tot))
#     denominator = (R_2 + (1 / (1j * freq * C_2)))
#     return np.real((numerator / denominator) * (1 / (1j * freq * C_2)))
#
#
# x = np.linspace(0, 1, 100000)
# y = v(x)
# plt.plot(x, y)
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("$V_{C_2}/V_1$")
# plt.show()

def z(freq):
    Z = 10 + (1j * 2 * np.pi * 10 * 10 ** (-3) * freq)
    return np.abs(Z)


x = np.linspace(0, 10, 10000)
plt.plot(x, z(x))
plt.xlabel("Frequency (Hz)")
plt.ylabel("$|Z|$")
plt.show()

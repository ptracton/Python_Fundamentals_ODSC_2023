#! /usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 100)
sin_wave = np.sin(x_vals)
cos_wave = np.cos(x_vals)

fig, ax = plt.subplots()

ax.plot(x_vals, sin_wave, "ro")
ax.plot(
    x_vals,
    cos_wave,
)
ax.legend(["sine", "cosine"])
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Plot Title")
plt.grid(True)
plt.show()

#! /usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 100)
sin_wave = np.sin(x_vals)
cos_wave = np.cos(x_vals)

fig, axs = plt.subplots(2, sharex=True, sharey=True)
fig.suptitle("Sharing both axes")
axs[0].plot(x_vals, sin_wave, "g")
axs[1].plot(x_vals, cos_wave, "r")
plt.show()

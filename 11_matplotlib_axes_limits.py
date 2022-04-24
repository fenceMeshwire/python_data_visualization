#!/usr/bin/env python3

# Python 3.9.5

# 11_matplotlib_axes_limits.py

# Dependencies
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100) # Start, Stop, Iteration
y = np.linspace(0, 0.5, 100) # Start, Stop, Iteration

# Parameters
plt.plot(x, y)
plt.xlim(-1, 11) # x_min, x_max
plt.ylim(-1.5, 1.5) # y_min, y_max

plt.show()

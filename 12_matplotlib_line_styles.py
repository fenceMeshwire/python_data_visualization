#!/usr/bin/env python3

# Python 3.9.5

# 12_matplotlib_line_styles.py

# Dependencies
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 1000)

# Operations
plt.plot(x, x + 1, linestyle='-') # solid
plt.plot(x, x + 2, linestyle='--') # dashed
plt.plot(x, x + 3, linestyle='-.') # dashdot
plt.plot(x, x + 4, linestyle=':'); # dotted

plt.show()

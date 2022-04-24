#!/usr/bin/env python3

# Python 3.9.5

# 10_matplotlib_colors.py

# Dependency
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 1000)

# Style
plt.style.use('seaborn-whitegrid')

# Define figure and axes
figure = plt.figure()
axes = plt.axes()

# Operations
plt.plot(x, np.sin(x - 0), color='#00AA22') # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 1), color='#001122') # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 2), color='#AA1122') # Hex code (RRGGBB from 00 to FF)

plt.show()

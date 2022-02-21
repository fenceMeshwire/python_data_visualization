#!/usr/bin/env python3

# Python 3.9.5

# 04_vertical_bar_graph.py

# Purpose: Visualization of data with a vertical bar graph using the module matplotlib.

# Dependencies
import matplotlib.pyplot as plt
import random

# Data
x = [1, 2, 3, 4, 5]
y = [random.randint(10, 50) for _ in range(5)]

# Visualization
label = ['Random data']
plt.bar(x, y)
plt.xticks(rotation=90)
plt.legend(label, loc='upper right')
plt.show()

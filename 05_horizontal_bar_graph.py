#!/usr/bin/env python3

# Python 3.9.5

# 05_horizontal_bar_graph.py

# Purpose: Visualization of data with a horizontal bar graph

# Dependencies
import matplotlib.pyplot as plt
import random

# Data
x = [1, 2, 3, 4, 5]
y = [random.randint(10, 50) for _ in range(5)]

# Visualization
label = ['Random data']
plt.barh(x, y)
plt.xticks(rotation=90)
plt.legend(label, loc='lower right')
plt.show()

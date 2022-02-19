#!/usr/bin/env python3

# Python 3.9.5

# 03_multiline_graph.py

# Purpose: Drawing a multiline graph

# Dependencies
import math
import matplotlib.pyplot as plt
import numpy as np

# Producing data with the functions sin(x), cos(x):
x = np.arange(0, 15, 0.1)
sin_x = [math.sin(i) for i in x]
cos_x = [math.cos(i) for i in x]

# Setting parameters for mutiline graph visualization:
labels = ['sin(x)', 'cos(x)']
plt.plot(x, sin_x)
plt.plot(x, cos_x)
plt.legend(labels, loc='lower right')
plt.grid()
plt.show()

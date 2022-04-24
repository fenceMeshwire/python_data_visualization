#!/usr/bin/env python3

# Python 3.9.5

# 00_introductions.py

# Dependency
import matplotlib.pyplot as plt

# Set style
plt.style.use('classic')

figure = plt.figure()

# Show available filetypes, return value is a dictionary
figure.canvas.get_supported_filetypes()

# Save the desired figure
figure.savefig('figure.jpg')

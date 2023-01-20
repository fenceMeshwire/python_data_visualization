#!/usr/bin/env python3

# Python 3.9.5

# Dependencies
import pandas as pd
import random
import matplotlib.pyplot as plt

# Generate data with a Pandas DataFrame
data = pd.DataFrame({
    'Alpha': [random.randint(10, 20) for i in range(5)], 
    'Beta': [random.randint(10, 20) for i in range(5)], 
    'Gamma': [random.randint(10, 20) for i in range(5)]})

# Plot the vertical bar chart
data.plot.bar()

# Show the bar chart
plt.show()

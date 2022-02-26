#!/usr/bin/env python3

# Python 3.9.5

# 07_DataFrame_Series_Visualization.py

# Dependencies
import pandas as pd
import matplotlib.pyplot as plt
data = {}

index = range(1, 9)
index = [counter for counter in range(1, 9)]

for i in range(1, 9):
    # Index takes <class 'range'> or <class 'list'> as input
    column = pd.Series(range(i, i * 8 + 1, i), index=index)
    data[i] = column # Add column to data dict.

mult_table = pd.DataFrame(data, index=index)
mult_table # Prints out the DataFrame 

 # Create a vertical bar chart for visualization
mult_table.plot.bar()
plt.grid()
plt.show()

# Find a value in the DataFrame, e.g. 4th row, 5th value
result = mult_table.loc[4, 5]
result # Check result with vertical bar chart

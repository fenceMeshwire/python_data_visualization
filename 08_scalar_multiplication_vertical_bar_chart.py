#!/usr/bin/env python3

# Python 3.9.5

# 08_scalar_multiplication_vertical_bar_chart.py

# Dependencies:
import matplotlib.pyplot as plt
import pandas as pd

# Data
articles = ['Part 1', 'Part 2', 'Part 3', 'Part 4', 'Part 5', 'Part 6']
unit_prices = [479, 250, 125, 100, 600, 400] 
quantities = [2, 2, 3, 8, 2, 3]

total_prices = [unit_prices[i] * quantities[i] for i in range(len(unit_prices))]

data = {
  "unit price": unit_prices,
  "total price": total_prices
}

df = pd.DataFrame(data, index=articles)
df.plot.bar()

plt.xticks(rotation=90)
plt.grid()
plt.show()

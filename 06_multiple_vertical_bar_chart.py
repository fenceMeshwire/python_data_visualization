#!/usr/bin/env python3

# Python 3.9.5

# multiple_vertical_bar_chart.py

# Dependencies:
import matplotlib.pyplot as plt
import pandas as pd

# Data
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
price = [5.35, 4.68, 3.29, 2.73, 3.73, 2.34, 2.7] 
quantity = [2.447, 2.135, 1.478, 1.148, 1.565, 1.030, 1.124]

data = {
  "price": price,
  "quantity": quantity
}

df = pd.DataFrame(data, index=years)
df.plot.bar()

plt.grid()
plt.show()

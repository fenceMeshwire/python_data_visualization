#!/usr/bin/env python3

# Python 3.9.5

# Display of the game results in a diagram

# Dependencies
import numpy as np
import matplotlib.pyplot as plt

# Game results, data
PLAYER1 = [1, 1, 1, 1, 3, 2, 2, 2, 1, 3, 3, 1, 2, 3, 2, 3, 1, 1]
PLAYER2 = [3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 1, 1, 3, 3, 1, 1]

# Operations
x = np.arange(1, len(PLAYER1) + 1)
p1 = np.array(PLAYER1)
p2 = np.array(PLAYER2)
# Summarize game results with cumulative sum
sum_p1 = np.cumsum(PLAYER1)
sum_p2 = np.cumsum(PLAYER2)

# Visualization
plt.xticks(x)
plt.plot(x, sum_p1,'*--', color='red')
plt.plot(x, sum_p2,'H--', color='blue')
plt.legend(['Player 1', 'Player 2'])
plt.title('Game results')
plt.show()

# optional save operation
# plt.savefig('filename.png') 

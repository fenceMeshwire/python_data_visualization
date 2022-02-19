#!/usr/bin/env python3

# Python 3.9.5

# Dependencies
import networkx as nx
import matplotlib.pyplot as plt

GRAPH = nx.path_graph(4)
locations = {0: 'Miami', 1: 'Atlanta', 2: 'Charlotte', 3:'Washington'}

LABELED_GRAPH = nx.relabel_nodes(GRAPH, locations)

nx.draw(LABELED_GRAPH, with_labels=True)
plt.show()

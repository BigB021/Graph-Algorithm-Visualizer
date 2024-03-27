# Author: Youssef AITBOUDDROUB
# main script
import tkinter as tk
from tkinter import ttk
from search_algorithms import SearchAlgorithms
from utility_class import GraphVisualizer 

# Instantiating the graph from SearchAlgorithms
graph = SearchAlgorithms(graph_type='undirected')
# Adding nodes and edges to  the graph
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'D', 3)
graph.add_edge('B', 'E', 4)
graph.add_edge('C', 'F', 5)
graph.add_edge('C', 'G', 6)
graph.add_edge('D', 'H', 7)
graph.add_edge('E', 'H', 8)
graph.add_edge('F', 'I', 9)
graph.add_edge('G', 'I', 10)
graph.add_edge('H', 'J', 11)
graph.add_edge('I', 'J', 12)
graph.add_edge('J', 'K', 13)

# Instantiate the GraphVisualizer with the graph
visualizer = GraphVisualizer(graph)

# Buttons to trigger search algorithms visualization
bfs_button = ttk.Button(visualizer.root, text="Visualize BFS", command=lambda: visualizer.visualize_bfs('A', 'K'))
bfs_button.pack(pady=5)

dfs_button = ttk.Button(visualizer.root, text="Visualize DFS", command=lambda: visualizer.visualize_dfs('A', 'K'))
dfs_button.pack(pady=5)

ucs_button = ttk.Button(visualizer.root, text="Visualize UCS", command=lambda: visualizer.visualize_ucs('A', 'K'))
ucs_button.pack(pady=5)

dls_button = ttk.Button(visualizer.root, text="Visualize DLS", command=lambda: visualizer.visualize_dls('A', 'C', 3))
dls_button.pack(pady=5)

ids_button = ttk.Button(visualizer.root, text="Visualize IDS", command=lambda: visualizer.visualize_ids('A', 'C', 3))
ids_button.pack(pady=5)

# Terminating on closing protocol
visualizer.root.protocol("WM_DELETE_WINDOW", visualizer.on_closing)

# Starting the Tkinter event loop
visualizer.root.mainloop()

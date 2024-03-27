# Author: Youssef AITBOUDDROUB
# Utility class script: converting and visualizing methods
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
from search_algorithms import SearchAlgorithms

class GraphVisualizer:
    def __init__(self, search_algo_graph):
        self.G = self.to_networkx_graph(search_algo_graph)
        self.root = tk.Tk()
        self.root.title("Graph Algorithms Visualizer")
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = None
        self.setup_canvas()
        self.initial_draw()
        # Storing the instance
        self.search_algo = search_algo_graph


    @staticmethod
    def to_networkx_graph(search_algo_graph):
        """
        Converts a graph from the SearchAlgorithms class into a NetworkX graph.

        Parameters:
        - search_algo_graph: An instance of the SearchAlgorithms class.

        Returns:
        A NetworkX graph object.
        """
        # Determine the graph type: directed or undirected
        G = nx.DiGraph() if search_algo_graph.graph_type == 'directed' else nx.Graph()
        # Add edges and weights to the NetworkX graph
        for from_node, to_nodes in search_algo_graph.graph.items():
            for to_node, weight in to_nodes.items():
                G.add_edge(from_node, to_node, weight=weight)
        return G

    def setup_canvas(self):
        """
        Embeds the Matplotlib figure into the Tkinter window and sets up the GUI.
        """
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.pack()

    def initial_draw(self):
        """
        Draws the initial graph with no path highlighted.
        """
        self.update_graph()

    def update_graph(self, path=[], node_c='lightgreen', edge_c='green'):
        """
        Updates the graph visualization.
        """
        self.ax.clear()  # Clear previous drawing
        pos = nx.spring_layout(self.G)  # Position nodes using Fruchterman-Reingold force-directed algorithm
        nx.draw(self.G, pos, ax=self.ax, with_labels=True, node_size=700, node_color="skyblue")
        
        # Highlight the path if given
        if path:
            nx.draw_networkx_nodes(self.G, pos, nodelist=path, node_color=node_c, ax=self.ax)
            edges = [(path[n], path[n+1]) for n in range(len(path)-1)]
            nx.draw_networkx_edges(self.G, pos, edgelist=edges, edge_color=edge_c, width=2, ax=self.ax)
        
        self.canvas.draw()

    def on_closing(self):
        """
        Properly closes the window and terminates the script.
        """
        self.root.quit()
        self.root.destroy()
        
    # Execution and visualization methods for each search algorithm 
    def visualize_bfs(self, start_node='A', goal_node='K'):
        path = self.search_algo.BFS(start_node, goal_node)
        self.update_graph(path, 'lightgreen', 'green')

    def visualize_dfs(self, start_node='A', goal_node='K'):
        path = self.search_algo.DFS(start_node, goal_node)
        self.update_graph(path, 'lightblue', 'blue')

    def visualize_ucs(self, start_node='A', goal_node='K'):
        path = self.search_algo.UCS(start_node, goal_node)
        self.update_graph(path, 'lightcoral', 'red')

    def visualize_dls(self, start_node='A', goal_node='C', depth_limit=3):
        found, path = self.search_algo.DLS(start_node, goal_node, depth_limit)
        if found:
            self.update_graph(path, 'lightyellow', 'orange')
        else:
            print("No path found within the depth limit.")

    def visualize_ids(self, start_node='A', goal_node='C', depth_limit=3):
        path = self.search_algo.IDS(start_node, goal_node, depth_limit)
        if path:
            self.update_graph(path, 'lightyellow', 'orange')
        else:
            print("No path found within the depth limit.")


    

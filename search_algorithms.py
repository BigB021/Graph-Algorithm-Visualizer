# Author : Youssef AITBOUDDROUB
# Basic implementation of the search algorithms using object oriented approach

from collections import deque
import heapq

class SearchAlgorithms:
    def __init__(self, graph_type='directed', graph=None):
        ''' Class Constructor '''
        self.graph = {} if graph is None else graph
        self.graph_type = graph_type

    def add_node(self, node):
        ''' Adds a new vertex to the graph '''
        # Initialize the node with an empty dictionary if it doesn't exist.
        if node not in self.graph:
            self.graph[node] = {}
            
    def add_edge(self, from_node, to_node, weight=1):
        ''' Adds a new edge to the graph'''
        if from_node not in self.graph:
            self.graph[from_node] = {}
        self.graph[from_node][to_node] = weight
        # Adds the edge in the opposite direction as well for undirected graphs
        if self.graph_type == 'undirected':
            if to_node not in self.graph:
                self.graph[to_node] = {}
            self.graph[to_node][from_node] = weight


    def BFS(self, start, goal=None):
        ''' Breath-First Search Algorithm that returns a path '''
        visited, queue = set(), deque([(start, None)])  # Each item is a tuple (node, predecessor)
        pred = {start: None}  # Predecessor map

        while queue:
            vertex, _ = queue.popleft()
            if vertex == goal:
                break  # Stop search once the goal is found
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append((neighbor, vertex))
                        pred[neighbor] = vertex  # Map neighbor to its predecessor

        if goal is not None and goal in visited:
            # Reconstruct path from goal to start using the predecessor map
            path = []
            while goal:
                path.append(goal)
                goal = pred[goal]
            return path[::-1]  # Return reversed path

        return list(visited)  # Return list of visited nodes if goal is None


    def UCS(self, start, goal=None):
            visited, priority_queue = set(), [(0, start, [])]
            while priority_queue:
                cost, current_vertex, path = heapq.heappop(priority_queue)
                if current_vertex == goal:
                    return path + [current_vertex]
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    for neighbor, weight in self.graph.get(current_vertex, {}).items():
                        if neighbor not in visited:
                            heapq.heappush(priority_queue, (cost + weight, neighbor, path + [current_vertex]))
            return []


    def DFS(self, start, goal=None):
        ''' Depth-First Search Algorithm that returns a path '''
        def dfs_visit(node, goal, visited, path):
            if node == goal:
                return True, path + [node]  # Return path on success
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    success, result_path = dfs_visit(neighbor, goal, visited, path + [node])
                    if success:
                        return True, result_path
            return False, path

        visited = set()
        success, path = dfs_visit(start, goal, visited, [])
        if goal is None:
            return list(visited)  # Return visited nodes if no goal
        if success:
            return path
        else:
            return []  # Return empty list if goal not found

    def DLS(self, start, goal, limit):
        def recursive_dls(node, goal, limit):
            if limit < 0:
                return False, []
            if node == goal:
                return True, [node]
            for neighbor in self.graph.get(node, []):
                found, path = recursive_dls(neighbor, goal, limit - 1)
                if found:
                    return True, [node] + path
            return False, []
        
        found, path = recursive_dls(start, goal, limit)
        return found, path  # Return the tuple


    def IDS(self, start, goal, max_depth):
        for limit in range(max_depth + 1):
            found, path = self.DLS(start, goal, limit)  # Call DLS on self
            if found:
                return path
        return []

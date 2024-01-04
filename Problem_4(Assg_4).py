from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def dfs_util(self, v, visited):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def count_trees(self):
        visited = set()
        count = 0

        for vertex in self.graph:
            if vertex not in visited:
                self.dfs_util(vertex, visited)
                count += 1

        return count

# Example usage:
if __name__ == "__main__":
    forest = Graph()
    forest.add_edge(0, 1)
    forest.add_edge(2, 3)
    forest.add_edge(4, 5)
    forest.add_edge(6, 7)

    print("Number of trees in the forest:", forest.count_trees())


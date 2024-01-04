from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def detect_cycle_util(self, v, visited, rec_stack):
        visited.add(v)
        rec_stack.add(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                if self.detect_cycle_util(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(v)
        return False

    def has_cycle(self):
        visited = set()
        rec_stack = set()

        for vertex in self.graph:
            if vertex not in visited:
                if self.detect_cycle_util(vertex, visited, rec_stack):
                    return True

        return False

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    if g.has_cycle():
        print("The directed graph has a cycle.")
    else:
        print("The directed graph doesn't have a cycle.")


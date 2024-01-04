from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def count_nodes_at_level(self, level):
        if not self.root:
            return 0
        
        queue = deque([(self.root, 1)])  # Using a tuple to track the node and its level
        nodes_at_level = 0

        while queue:
            node, node_level = queue.popleft()

            if node_level == level:
                nodes_at_level += 1

            if node.left:
                queue.append((node.left, node_level + 1))
            if node.right:
                queue.append((node.right, node_level + 1))

        return nodes_at_level

# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.right = Node(8)
    tree.root.right.right.left = Node(6)
    tree.root.right.right.right = Node(7)

    print("Displaying the created tree:")
    # tree.display_tree()  # Uncomment to display the tree (if display_tree method exists)

    level_to_count = 3
    count = tree.count_nodes_at_level(level_to_count)
    print(f"Number of nodes at level {level_to_count}: {count}")


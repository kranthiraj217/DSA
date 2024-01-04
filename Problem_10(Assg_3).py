class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self):
        self.root = None

    # Other methods remain unchanged...
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self.insert_recursive(self.root, key)
    
    def insert_recursive(self, root, key):
        if key < root.val:
            if root.left:
                self.insert_recursive(root.left, key)
            else:
                root.left = Node(key)
        else:
            if root.right:
                self.insert_recursive(root.right, key)
            else:
                root.right = Node(key)
    
    def display_tree(self):
        if not self.root:
            return
        
        nodes = [(self.root, 0)]
        current_level = 0
        
        while nodes:
            node,level = nodes.pop(0)
            
            if level > current_level:
                print()
                current_level = level
            print(node.val,end=" ")
            
            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))
        print("\n")

    def print_odd_level_nodes(self):
        if not self.root:
            return
        
        queue = [(self.root, 1)]  # Using a tuple to track the node and its level

        while queue:
            node, level = queue.pop(0)

            if level % 2 != 0:
                print(node.val, end=" ")

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

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
    tree.display_tree()

    print("Nodes at odd levels:")
    tree.print_odd_level_nodes()



class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if key < root.val:
            if root.left:
                self._insert_recursive(root.left, key)
            else:
                root.left = Node(key)
        else:
            if root.right:
                self._insert_recursive(root.right, key)
            else:
                root.right = Node(key)
                
    def display_tree(self):
        if not self.root:
            print("Tree is empty.")
            return

        nodes = [(self.root, 0)]
        current_level = 0

        while nodes:
            node, level = nodes.pop(0)

            if level > current_level:
                print()
                current_level = level

            print(node.val, end=" ")

            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))

        print("\n")

    
    def height_of_tree(self, node):
        if node is None:
            return -1  # Height of an empty tree is -1 by convention
        else:
            left_height = self.height_of_tree(node.left)
            right_height = self.height_of_tree(node.right)

            return max(left_height, right_height) + 1

# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    print("Displaying the created tree:")
    tree.display_tree()
    
    print("Height of the tree:", tree.height_of_tree(tree.root))
    

#Find sum of all left leaves in a given Binary Tree

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

    def sum_left_leaves(self, node):
        if node is None:
            return 0

        left_sum = 0

        if node.left:
            if node.left.left is None and node.left.right is None:
                left_sum += node.left.val  # Add value if it's a left leaf
            else:
                left_sum += self.sum_left_leaves(node.left)  # Recurse for left subtree

        left_sum += self.sum_left_leaves(node.right)  # Recurse for right subtree

        return left_sum

# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(50)
    tree.root.left = Node(30)
    tree.root.right = Node(70)
    tree.root.left.left = Node(20)
    tree.root.left.right = Node(40)
    tree.root.right.left = Node(60)
    tree.root.right.right = Node(80)

    print("Displaying the created tree:")
    tree.display_tree()

    left_leaves_sum = tree.sum_left_leaves(tree.root)
    print("Sum of left leaves in the tree:", left_leaves_sum)


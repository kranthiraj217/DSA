class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

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
    
    def display(self):
        if not self.root:
            print("Empty tree")
            return
        
        nodes = [(self.root, 0)]
        current_level = 0
        
        while nodes:
            node, level = nodes.pop(0)
            
            if level > current_level:
                print()
                current_level = level
            
            print(node.val,end=" ")
            
            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))
        
        print("\n")
    
    def print_leaves(self, node):
        if node:
            if node.left is None and node.right is None:
                print(node.val, end=" ")
            self.print_leaves(node.left)
            self.print_leaves(node.right)
            
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)
    tree.insert(34)

    print("Displaying the created tree:")
    tree.display()
    
    print("\nLeaf nodes in the tree:")
    tree.print_leaves(tree.root)

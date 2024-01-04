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

     def preorder(self, root):
        if root:
            print(root.val,end= " ")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val,end=" ")
            self.inorder(root.right)
    
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val,end=" ")

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
    
     print("\nPreorder Traversal : ")
    tree.preorder(tree.root)
    
    print("\nInorder Traversal : ")
    tree.inorder(tree.root)
    
    print("\nPostorder Traversal : ")
    tree.postorder(tree.root)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class PerfectBinaryTree:
    def __init__(self):
        self.root = None

    def insert_nodes(self, arr, root, i, n):
        if i < n:
            temp = Node(arr[i])
            root = temp
            root.left = self.insert_nodes(arr, root.left, 2 * i + 1, n)
            root.right = self.insert_nodes(arr, root.right, 2 * i + 2, n)
        return root

    def sum_of_nodes(self, root):
        if not root:
            return 0
        return root.val + self.sum_of_nodes(root.left) + self.sum_of_nodes(root.right)

    def display_tree(self):
        if not self.root:
            return -1
        
        nodes = [(self.root, 0)]
        current_level = 0
        
        while nodes:
            node,level = nodes.pop(0)
            
            if level > current_level:
                print()
                current_level = level
            print(node.val,end=" ")
            
            if node.left:
                nodes.append((node.left, level+1))
            if node.right:
                nodes.append((node.right, level + 1))
        print("\n")

# Example usage:
if __name__ == "__main__":
    perfect_tree = PerfectBinaryTree()
    tree_values = [1, 2, 3, 4, 5, 6, 7]
    tree_height = 2  # Example height of the perfect binary tree (0-indexed)

    # Calculating the total number of nodes for the perfect binary tree of given height
    num_of_nodes = 2 ** (tree_height + 1) - 1

    # Inserting values into the tree
    perfect_tree.root = perfect_tree.insert_nodes(tree_values, perfect_tree.root, 0, len(tree_values))

    print("Displaying the created perfect binary tree:")
    perfect_tree.display_tree()

    sum_of_all_nodes = perfect_tree.sum_of_nodes(perfect_tree.root)
    print("Sum of all nodes in the perfect binary tree:", sum_of_all_nodes)


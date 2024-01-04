
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

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

    def count_subtrees_with_sum(self, node, target_sum):
        if node is None:
            return 0

        left_sum = self.count_subtrees_with_sum(node.left, target_sum)
        right_sum = self.count_subtrees_with_sum(node.right, target_sum)

        current_sum = node.val + left_sum + right_sum

        if current_sum == target_sum:
            self.count += 1

        return current_sum

    def count_subtrees(self, target_sum):
        self.count = 0
        self.count_subtrees_with_sum(self.root, target_sum)
        return self.count

# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(4)
    tree.root.right = Node(8)
    tree.root.left.left = Node(11)
    tree.root.left.left.left = Node(7)
    tree.root.left.left.right = Node(2)
    tree.root.right.left = Node(13)
    tree.root.right.right = Node(4)
    tree.root.right.right.right = Node(1)

    print("Displaying the created tree:")
    tree.display_tree()

    target_sum = 20
    count_of_subtrees = tree.count_subtrees(target_sum)
    print(f"Number of subtrees with sum {target_sum}: {count_of_subtrees}")


from collections import deque

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

    def max_level_sum(self):
        if not self.root:
            return 0
        
        max_sum = float('-inf')  # Initialize with negative infinity to compare sums
        max_level = 0
        level = 0
        
        queue = deque()
        queue.append(self.root)

        while queue:
            level += 1
            level_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

        return max_level, max_sum

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

    level, max_sum = tree.max_level_sum()
    print(f"Maximum level sum is at level {level} with sum {max_sum}")


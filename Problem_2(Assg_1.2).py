class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def reverse_in_groups(self, head, k):
        current = head
        next_node = None
        prev = None
        count = 0

        # Reverse k elements of the linked list
        while current and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1

        # Recursive call for the remaining list
        if next_node:
            head.next = self.reverse_in_groups(next_node, k)

        return prev

    def reverse_linked_list_in_groups(self, k):
        self.head = self.reverse_in_groups(self.head, k)

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Example usage:
my_list = LinkedList()
elements = [1, 2, 3, 4, 5, 6, 7, 8]
for element in elements:
    my_list.insert(element)

group_size = 3  # Change this value to your desired group size
print("Original Linked List:")
my_list.display()

my_list.reverse_linked_list_in_groups(group_size)
print(f"\nLinked List after Reversing in Groups of {group_size}:")
my_list.display()


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

    def merge_at_alternate_positions(self, second_list):
        current = self.head
        second_current = second_list.head

        while current and second_current:
            next_node = current.next
            second_next = second_current.next

            current.next = second_current
            second_current.next = next_node

            current = next_node
            second_current = second_next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Example usage:
list1 = LinkedList()
list2 = LinkedList()

elements1 = [1, 3, 5, 7]
elements2 = [2, 4, 6, 8]

for element in elements1:
    list1.insert(element)

for element in elements2:
    list2.insert(element)

print("List 1:")
list1.display()
print("List 2:")
list2.display()

list1.merge_at_alternate_positions(list2)
print("\nMerged List at Alternate Positions:")
list1.display()


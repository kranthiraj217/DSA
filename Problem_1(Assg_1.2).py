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
            print("temp data : ", temp.data)

    def delete_zero_sum(self):
        current = self.head
        while current:
            sum_val = current.data
            temp = current.next

            while temp:
                sum_val += temp.data
                if sum_val == 0:
                    current.next = temp.next
                    temp = current
                    break
                temp = temp.next
            current = current.next
            print("sum_val :", sum_val)

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Example usage:
my_list = LinkedList()
#elements = [1,-5,12,8,-4,-11,15]
elements = [6, -6, 8, 4, -12, 9, 8, -8]
for element in elements:
    my_list.insert(element)

print("Original Linked List:")
my_list.display()

my_list.delete_zero_sum()
print("\nLinked List after Deleting Elements with Zero Sum:")
my_list.display()


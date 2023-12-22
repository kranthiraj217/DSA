class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def reverse_stack(self):
        if not self.is_empty():
            temp = self.pop()
            self.reverse_stack()
            self._insert_at_bottom(temp)

    def _insert_at_bottom(self, item):
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self._insert_at_bottom(item)
            self.push(temp)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Original Stack:", stack.items)
stack.reverse_stack()
print("Reversed Stack:", stack.items)


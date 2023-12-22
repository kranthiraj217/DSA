class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] if self.stack2 else None

    def is_empty(self):
        return not self.stack1 and not self.stack2

# Example usage:
queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeued item:", queue.dequeue())
print("Peeked item:", queue.peek())
print("Is the queue empty?", queue.is_empty())


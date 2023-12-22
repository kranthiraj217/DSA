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

def evaluate_postfix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        elif char in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(char, operand1, operand2)
            stack.push(result)

    return stack.pop()

def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            raise ValueError("Division by zero error")
        return operand1 // operand2  # For integer division in Python

# Example usage:
postfix_expression = "62/31-41+3*"
result = evaluate_postfix(postfix_expression)
print("Result of Postfix Expression Evaluation:", result)


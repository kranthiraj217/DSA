def is_operator(char):
    return char in '+-*/^'

def prefix_to_infix(prefix):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    
    for char in reversed(prefix):
        if not is_operator(char):  # Operand
            stack.append(char)
        else:  # Operator
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f"({operand1}{char}{operand2})")  # Combine operands with the operator
    
    return stack.pop()

# Example usage:
prefix_expr = "*+AB-CD"
infix_expr = prefix_to_infix(prefix_expr)
print("Prefix Expression:", prefix_expr)
print("Infix Expression:", infix_expr)


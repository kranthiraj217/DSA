def postfix_to_prefix(postfix):
    stack = []
    
    for char in postfix:
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)  # Combine operands with the operator
    
    return stack.pop()

# Example usage:
postfix_expr = "AB+CD-*"
prefix_expr = postfix_to_prefix(postfix_expr)
print("Postfix Expression:", postfix_expr)
print("Prefix Expression:", prefix_expr)

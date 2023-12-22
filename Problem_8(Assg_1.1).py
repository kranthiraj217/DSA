def are_brackets_balanced(code):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            # If the stack is empty or the closing bracket doesn't match the corresponding opening bracket
            if not stack or opening_brackets[closing_brackets.index(char)] != stack.pop():
                return False
    
    # If there are any unclosed brackets left in the stack
    return not stack

# Example usage:
code_snippet = "{(a+b)*(c-d)}"
if are_brackets_balanced(code_snippet):
    print("Brackets are balanced in the code snippet.")
else:
    print("Brackets are not balanced in the code snippet.")


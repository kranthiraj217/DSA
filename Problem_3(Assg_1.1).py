def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    concatenated = str1 + str1

    # Check if str2 is a substring of the concatenated string
    if str2 in concatenated:
        return True
    else:
        return False

# Example usage:
string1 = "abcd"
string2 = "cdab"

if are_rotations(string1, string2):
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")


def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

# Example usage:
array = [1, 2, 3, 4, 2, 3, 5]
duplicate_elements = find_duplicates(array)
if duplicate_elements:
    print("Duplicate elements:", duplicate_elements)
else:
    print("No duplicates found.")


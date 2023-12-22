def move_negatives(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] > 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] > 0 and arr[right] > 0:
            right -= 1
        else:
            left += 1
            right -= 1

# Example usage:
array = [1, -2, 3, -4, 5, -6, 7, -8, -9]
print("Original Array:", array)

move_negatives(array)
print("Array with Negative Elements Moved to One Side:", array)


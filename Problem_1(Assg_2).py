def binary_search(arr, target):
    sorted_arr = sorted(arr)
    left = 0
    right = len(sorted_arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

a = [5,1,11,2,3,9,6,4,10]
target = 4

result = binary_search(a, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

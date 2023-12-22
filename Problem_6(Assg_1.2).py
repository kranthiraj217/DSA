def kth_largest_smallest(arr, k):
    if k > len(arr) or k <= 0:
        return None

    sorted_arr = sorted(arr)
    kth_largest = sorted_arr[-k]
    kth_smallest = sorted_arr[k - 1]

    return kth_largest, kth_smallest

# Example usage:
array = [3, 1, 5, 7, 2, 4, 6]
k = 3

kth_largest, kth_smallest = kth_largest_smallest(array, k)

if kth_largest is not None and kth_smallest is not None:
    print(f"{k}th Largest Number: {kth_largest}")
    print(f"{k}th Smallest Number: {kth_smallest}")
else:
    print("Invalid value of k or array length.")

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)

a = [10,6,9,2,5,1,3,7]
print("Original Array : ", a)
quick_sort(a, 0, len(a) - 1)
print("Sorted Array : ", a)

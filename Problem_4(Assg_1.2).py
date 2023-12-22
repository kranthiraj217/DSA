def count_pairs_with_sum(arr, target_sum):
    count = 0
    hash_map = {}

    for num in arr:
        complement = target_sum - num
        if complement in hash_map:
            count += hash_map[complement]
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    return count

# Example usage:
array = [1, 5, 7, -1, 5]
sum_value = 6

result = count_pairs_with_sum(array, sum_value)
print(f"The number of pairs with sum {sum_value} is: {result}")

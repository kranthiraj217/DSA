def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs

# Example usage:
array = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
sum_value = 7

result_pairs = find_pairs_with_sum(array, sum_value)
if result_pairs:
    print(f"The pairs with sum {sum_value} are:")
    for pair in result_pairs:
        print(pair)
else:
    print("No pairs found with the given sum.")


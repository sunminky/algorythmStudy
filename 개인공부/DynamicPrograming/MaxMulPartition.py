def find_maximum(arr, n):
    if n <= 0:
        return -1111

    max_at = arr[0]  # Maximum value that ends at arr[i]
    min_at = arr[0]  # Minimum value that ends at arr[i]
    max_value = max_at;

    for i in range(n):
        prev_max_at = max_at
        prev_min_at = min_at
        max_at = max(arr[i], arr[i] * prev_min_at, arr[i] * prev_max_at)
        min_at = min(arr[i], arr[i] * prev_min_at, arr[i] * prev_max_at)
        max_value = max(max_value, max_at)

    return max_value

if __name__ == "__main__":
    answer = find_maximum([-6,12,-7,0,14,-7,5],7)
    print(answer)
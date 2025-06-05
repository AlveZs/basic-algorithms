# O(logn)
def binary_search(arr, n):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid_index = (start + end) // 2
        if arr[mid_index] == n:
            print(f'Index {mid_index}')
            return n
        if n > arr[mid_index]:
            start = mid_index + 1
        else:
            end = mid_index - 1
    return None

# O(logn)
def recursive_binary_search(arr, n, start, end):
    if start <= end:
        mid_index = (start + end) // 2
        if n == arr[mid_index]:
            print(mid_index);
            return n
        if n > arr[mid_index]:
            return recursive_binary_search(arr, n, mid_index + 1, end)
        else:
            return recursive_binary_search(arr, n, start, mid_index - 1)
    else:
        return None

# O(n)
def linear_search(arr, n):
    for i, value in enumerate(arr):
        if value == n:
            print(i)
            return value
    return None

n = int(input())
arr = list(map(int, input().split(',')))
print(n)
print(arr)
print(recursive_binary_search(arr, n, 0, len(arr) - 1))

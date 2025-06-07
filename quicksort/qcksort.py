def qcksort(arr):
    if len(arr) < 2:
        return arr
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    arr_without_pivot = arr[:pivot_index] +  arr[pivot_index + 1:];
    left = qcksort([i for i in arr_without_pivot if i <= pivot]);
    right = qcksort([i for i in arr_without_pivot if i > pivot]);

    return left + [pivot] + right

# Without one more array
def qcksort2(arr):
    if len(arr) < 2:
        return arr
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    left = qcksort([arr[i] for i in range(len(arr)) if arr[i] <= pivot and i != pivot_index])
    right = qcksort([arr[i] for i in range(len(arr)) if arr[i] > pivot and i != pivot_index])

    return left + [pivot] + right

def partition(arr, left, right):
    pivot_index = (left + right) // 2
    pivot_value = arr[pivot_index]
    curr_index = left - 1
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    for j in range(left, right):
        if arr[j] < pivot_value:
            curr_index += 1
            arr[j], arr[curr_index] = arr[curr_index], arr[j]
    arr[curr_index + 1], arr[right] = arr[right], arr[curr_index + 1]
    return curr_index + 1

# Real. Without auxiliary space
def quicksort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)

arr = list(map(int, input().split(',')));
print(arr);
quicksort(arr, 0, len(arr) - 1);
print(arr);
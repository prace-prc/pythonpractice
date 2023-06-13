def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key_item = arr[i]
        j = i - 1
        while j >= start and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item


def merge(arr, start, mid, end):
    if arr[mid] <= arr[mid + 1]:
        return

    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1


def timsort(arr):
    min_run = 4
    n = len(arr)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(start + size - 1, n - 1)
            end = min(start + 2 * size - 1, n - 1)
            merge(arr, start, mid, end)
        size *= 2

    return arr


a = ['f', 'g', 'h', 'z', 's', 'b', 'c', 'd']

print(timsort(a))

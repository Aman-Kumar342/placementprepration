def max_heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def min_heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] < arr[smallest]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


def heap_sort(arr, reverse=False):
    n = len(arr)
    if reverse:
        for i in range(n // 2 - 1, -1, -1):
            min_heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            min_heapify(arr, i, 0)
    else:
        for i in range(n // 2 - 1, -1, -1):
            max_heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            max_heapify(arr, i, 0)
    return arr


if __name__ == "__main__":
    data = [4, 10, 3, 5, 1]
    print(heap_sort(data.copy()))
    print(heap_sort(data.copy(), reverse=True))

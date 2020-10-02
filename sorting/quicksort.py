
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quicksort(arr, low, high):
    if not low < high: return
    pivot = partition(arr, low, high)
    quicksort(arr, low, pivot - 1)
    quicksort(arr ,pivot + 1, high)
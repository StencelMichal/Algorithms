
def partition(arr, low, high):
    x = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickselect( arr , id , low , high ):
    if not low < high:
        return arr[low]
    pivot = partition(arr , low , high)
    if id < pivot:
        return quickselect(arr , id , low , pivot-1)
    elif id > pivot:
        return quickselect(arr , id , pivot+1 , high)
    else:
        return arr[pivot]


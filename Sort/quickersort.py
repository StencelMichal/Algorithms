
def quickerSort( arr ):
    if len(arr) == 1:
        return arr
    if len(arr) == 0:
        return
    left = []
    mid = []
    right = []
    pivot = arr[0]

    for i in range(len(arr)):
        if arr[i] < pivot: left.append(arr[i])
        elif arr[i] > pivot: right.append(arr[i])
        else: mid.append(arr[i])

    left = quickerSort(left)
    right = quickerSort(right)

    res = []
    if left != None:
        res.extend(left)
    if mid != None:
        res.extend(mid)
    if right != None:
        res.extend(right)

    return res

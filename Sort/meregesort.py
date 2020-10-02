import random


def merege(A, B):
    i = 0
    j = 0
    res = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1

    if i < len(A):
        res.extend(A[i:len(A)])
    if j < len(B):
        res.extend((B[j:len(B)]))

    return res


def mergesort(arr):

    if len(arr) == 1:
        return arr

    left = []
    for i in range(0, len(arr) // 2):
        left.append(arr[i])
    left = mergesort(left)

    right = []
    for i in range(len(arr) // 2, len(arr)):
        right.append(arr[i])
    right = mergesort(right)

    return merege(left, right)


arr = [None] * 15
for i in range(15):
    arr[i] = random.randint(0, 15)
print(arr)
arr = mergesort(arr)
print(arr)

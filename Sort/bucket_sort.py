
def bucketSort( arr , buckets ):
    B = [[] for i in range(buckets+1)]
    x = max(arr)
    for elem in arr:
        id = (int)(elem / x * buckets)
        B[id].append(elem)
    for i in range(len(B)):
        if len(B[i]) > 1:
            insertionSort(B[i])
    i = 0
    for j in range(buckets+1):
        for k in range(len(B[j])):
            arr[i] = B[j][k]
            i += 1

def insertionSort( arr ):
    for i in range(1,len(arr)):
        while( i > 0 and arr[i-1] > arr[i]):
            arr[i-1] , arr[i] = arr [i] , arr[i-1]
            i -= 1


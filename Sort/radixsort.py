
def countsortRadix(A, D):
    k = max(A)
    B = [None] * len(A)
    C = [0] * (k+1)

    for num in A:
        C[num] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = D[i]
    for i in range(len(A)):
        D[i] = B[i]

def radixsort(arr):
    x = max(arr)
    iter = 0
    while x > 0:
        x = x // 10
        iter += 1
    p = 10
    for i in range(iter):
        A = []
        for i in range(len(arr)):
            A.append(((arr[i] - arr[i] % (p // 10)) // (p//10)) % 10)
        countsortRadix(A, arr)
        p *= 10

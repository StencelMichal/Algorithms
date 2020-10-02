
def countSort(A):
    maximum = max(A) + 1
    B = [None] * len(A)
    C = [0] * maximum

    for num in A:
        C[num] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(len(A)):
        A[i] = B[i]


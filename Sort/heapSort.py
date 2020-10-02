class Heap:
    def __init__(self, arr=None):
        if arr is None:
            self.arr = []
            self.length = 0
        else:
            self.arr = arr
            self.length = len(arr)
            self.buildHeap()

    def left(self, i):
        if 2 * i + 1 < self.length:
            return 2 * i + 1
        return None

    def right(self, i):
        if 2 * i + 2 < self.length:
            return 2 * i + 2
        return None

    def parent(self, i):
        if i != 0:
            return i // 2
        return None

    def heapify(self, i):

        l = self.left(i)
        r = self.right(i)
        tmp = i

        if l is not None:
            if self.arr[l] > self.arr[tmp]:
                tmp = l
        if r is not None:
            if self.arr[r] > self.arr[tmp]:
                tmp = r
        if tmp != i:
            self.arr[tmp], self.arr[i] = self.arr[i], self.arr[tmp]
            self.heapify(tmp)

    def buildHeap(self):
        for i in range(self.length // 2, -1, -1):
            self.heapify(i)

def heapSort(arr, reversed=False):

    heap = Heap(arr.copy())
    heap.buildHeap()

    for i in range(len(arr) - 1 , -1, -1):
        arr[i] = heap.arr[0]
        heap.arr[i] , heap.arr[0] = heap.arr[0] , heap.arr[i]
        heap.length -= 1
        heap.heapify(0)

    if not reversed:
        arr.reverse()



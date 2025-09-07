import heapq

class AbsoluteMaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val: int):
        heapq.heappush(self.heap, (-abs(val), val))

    def top(self) -> int:
        return self.heap[0][1]

    def pop(self):
        heapq.heappop(self.heap)

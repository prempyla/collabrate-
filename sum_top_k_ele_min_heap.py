import heapq

class Solution:
    def sum_of_top_k_elements(self, heap, k):
        total = 0
        for i in range(k):
            total += heapq.heappop(heap)
        return total

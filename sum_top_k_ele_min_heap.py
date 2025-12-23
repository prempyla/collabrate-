import heapq

class Solution:
    def sum_of_top_k_elements(self, heap, k):
        # code here
        total = 0
        for i in range(k):
            total += heapq.heappop(heap)
        return total

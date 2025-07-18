import heapq

def findKthLargest(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:  
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    return min_heap[0]

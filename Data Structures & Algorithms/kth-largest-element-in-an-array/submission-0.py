class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            else:
                curr_min = heap[0]
                if curr_min < x:
                    heapq.heappop(heap)
                    heapq.heappush(heap, x)
        return heap[0]
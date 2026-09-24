class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        left = 0
        for right in range(len(nums)):
            heapq.heappush(heap, (-nums[right], right))
            if right >= k - 1:
                left = right - k + 1
                while heap[0][1] < left:
                    heapq.heappop(heap)
                ans.append(-heap[0][0])
        return ans

            
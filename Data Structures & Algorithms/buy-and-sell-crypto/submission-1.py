class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float('inf')
        curr_max = -1
        ans = 0
        for p in prices:
            if p < curr_min:
                curr_min = min(curr_min, p)
                curr_max = -1
            else:
                curr_max = max(curr_max, p)
                ans = max(ans, curr_max - curr_min)
        return ans
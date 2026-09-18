class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_possible = 1
        max_possible = max(piles)
        ans = max_possible
        while min_possible <= max_possible:
            mid = (min_possible + max_possible) // 2
            expected_h = 0
            for p in piles:
                expected_h += math.ceil(p / mid)
            
            if expected_h <= h:
                max_possible = mid - 1
                ans = min(ans, mid)
            else:
                min_possible = mid + 1
        return ans
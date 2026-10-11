class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        hold = -prices[0]
        sold = float('-inf')
        rest = 0

        for p in prices[1:]:
            new_hold = max(hold, rest-p)
            new_sold = hold + p
            new_rest = max(rest, sold)

            hold, sold, rest = new_hold, new_sold, new_rest
        return max(hold, sold, rest)
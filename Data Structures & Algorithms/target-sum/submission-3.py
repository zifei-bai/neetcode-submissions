class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        m = sum(nums)
        n = len(nums)
        dp = [[0] * (2 * m + 1) for _ in range(n + 1)]
        
        if abs(target) > m:
            return 0

        dp[0][m] = 1
        for i in range(n + 1):
            for j in range(2 * m + 1):
                if i == 0:
                    continue
                if 0 <= j - nums[i - 1] < 2 * m + 1:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
                if 0 <= j + nums[i - 1] < 2 * m + 1:
                    dp[i][j] += dp[i - 1][j + nums[i - 1]]
        # print(dp)                
        return dp[n][target + m]
 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        temp_sum = 0
        for x in nums:
            if temp_sum < 0:
                temp_sum = 0
            temp_sum += x

            ans = max(ans, temp_sum)
        return ans
            
            

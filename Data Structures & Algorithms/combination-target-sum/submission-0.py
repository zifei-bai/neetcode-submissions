class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        curr_sum = 0
        curr_set = []
        def dfs(start):
            nonlocal curr_sum
            if curr_sum > target:
                return
            if curr_sum == target:
                ans.append(curr_set.copy())
                return
            
            for i in range(start, len(nums)):
                curr_sum += nums[i]
                curr_set.append(nums[i])
                dfs(i)
                curr_sum -= nums[i]
                curr_set.pop()
        
        dfs(0)
        return ans
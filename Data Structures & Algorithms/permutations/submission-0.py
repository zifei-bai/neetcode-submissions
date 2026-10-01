class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr_set = []

        def dfs():
            if len(nums) == 0:
                ans.append(curr_set.copy())
                return

            for i in range(len(nums)):
                curr_set.append(nums[i])
                nums.pop(i)
                dfs()
                popped = curr_set.pop()
                nums.insert(i, popped)
        dfs()
        return ans
    
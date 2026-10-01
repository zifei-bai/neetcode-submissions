class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        def dfs(i):
            if i >= len(nums):
                sorted_curr = sorted(curr.copy())
                if sorted_curr not in ans:
                    ans.append(sorted_curr)
                return
            
            curr.append(nums[i])
            dfs(i + 1)

            curr.pop()
            dfs(i + 1)

        dfs(0)
        return ans
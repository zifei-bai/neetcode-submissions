class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curr_sum = 0
        ans = []
        curr_set = []
        def dfs(start):
            nonlocal curr_sum
            if curr_sum == target:
                ans.append(curr_set.copy())
                return
            if start >= len(candidates):
                return
            if curr_sum > target:
                return
            

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                curr_sum += candidates[i]
                curr_set.append(candidates[i])
                dfs(i + 1)
                curr_sum -= candidates[i]
                curr_set.pop()
        
        dfs(0)
        return ans
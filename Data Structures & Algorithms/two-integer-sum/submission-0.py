class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        ans = []
        for i, x in enumerate(nums):
            if comp.get(target - x) is not None:
                # print(f'ans is:')
                ans = [comp[target - x], i]
                # print(ans)
            comp[x] = i
            # print(comp)
        return ans

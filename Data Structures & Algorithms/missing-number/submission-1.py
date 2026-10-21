class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hashset = set([x for x in range(n + 1)])
        for i in range(0, n):
            hashset.remove(nums[i])
        return list(hashset)[0]
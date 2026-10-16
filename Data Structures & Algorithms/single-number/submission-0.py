class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                seen.remove(n)
        return seen.pop()
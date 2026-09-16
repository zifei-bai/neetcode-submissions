class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hashset = set(nums)
        max_val = max(nums)
        # print(f'hashset: {hashset}\nmax_val: {max_val}')
        count = 0
        ans = 0
        for x in hashset:
            if x - 1 not in hashset:
                # print(f'x is {x}')
                count = 0
                for i in range(x, max_val+1):
                    if i in hashset:
                        count += 1
                    else:
                        break
                # print(f'count is {count}')
            ans = max(ans, count)
        return ans
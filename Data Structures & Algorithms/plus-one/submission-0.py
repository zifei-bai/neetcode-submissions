class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(d) for d in digits]
        string_num = "".join(digits)
        num = int(string_num)
        ans = num + 1
        ans = str(ans)
        ans = list(ans)
        ans = [int(d) for d in ans]
        return ans

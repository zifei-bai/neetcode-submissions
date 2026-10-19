class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            str_i = bin(i)[2:]
            list_i = list(str_i)
            list_i = [int(x) for x in list_i]
            ans.append(sum(list_i))
        return ans
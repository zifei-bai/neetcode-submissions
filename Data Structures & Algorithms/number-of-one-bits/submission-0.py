class Solution:
    def hammingWeight(self, n: int) -> int:
        bi = bin(n)
        num = list(bi[2:])
        # print(num)
        num = [int(ch) for ch in num]
        # print(num)
        return sum(num)
        
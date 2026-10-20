class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)[2:]
        bin_n = '0' * (32 - len(bin_n)) + bin_n
        reversed_n = bin_n[::-1]
        ans = 0
        for i, x in enumerate(reversed_n):
            if x == '1':
                ans += pow(2, 31 - i)
        return ans

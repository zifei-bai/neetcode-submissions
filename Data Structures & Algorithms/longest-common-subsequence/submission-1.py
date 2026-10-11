class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[0] * (n+1) for _ in range(m+1)]
        #print(memo)
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    continue
                if text1[i-1] == text2[j-1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        return memo[m][n]

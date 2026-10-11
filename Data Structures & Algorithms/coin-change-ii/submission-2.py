class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        # print(memo)
        for i in range(0, len(coins) + 1):
            for j in range(amount + 1):
                if j == 0:
                    memo[i][j] = 1
                if i == 0:
                    if j == 0:
                        memo[i][j] = 1
                    else:
                        continue
                else:
                    if j - coins[i-1] < 0:
                        memo[i][j] = memo[i - 1][j]
                    else:
                        memo[i][j] = memo[i - 1][j] + memo[i][j - coins[i-1]]

        return memo[len(coins)][amount]


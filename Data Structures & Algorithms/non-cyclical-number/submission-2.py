class Solution:
    def isHappy(self, n: int) -> bool:
        nn = n
        hashset = set()
        while True:
            nn = list(str(nn)) # ['1', '0', '0'] 
            ans = 0
            for i in nn:
                ans += int(i) ** 2
            if ans == 1:
                return True
            if ans in hashset:
                return False
            hashset.add(ans)
            nn = ans
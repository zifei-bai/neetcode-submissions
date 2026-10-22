class Solution:
    def isHappy(self, n: int) -> bool:
        nn = n
        # count = 0
        hashset = set()
        while True:
            # print(nn)
            nn = list(str(nn)) # ['1', '0', '0'] 
            # print(len(hashset))
            ans = 0
            for i in nn:
                ans += int(i) ** 2
            if ans == 1:
                return True
            if ans in hashset:
                return False
            hashset.add(ans)
            nn = ans
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opens = 0
        closes = 0
        ans = []
        temp = ""
        def dfs():
            nonlocal opens
            nonlocal closes
            nonlocal temp
            if opens == n and closes == n:
                ans.append(temp)
                return
            if opens > n:
                return
            
            if opens < n:
                temp += '('
                opens += 1
                dfs()
                temp = temp[:-1]
                opens -= 1
            if closes < opens:
                temp += ')'
                closes += 1  
                dfs()
                temp = temp[:-1]
                closes -= 1
        
        dfs()
        return ans
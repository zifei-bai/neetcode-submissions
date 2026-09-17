class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for char in s:
            if char.isalpha() or char.isdigit():
                continue
            else:
                s = s.replace(char, '')

        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
                
        return True
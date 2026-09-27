class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if stack:
                    last = stack.pop()
                    if hashmap[char] != last:
                        return False
                else:
                    return False
        
        if stack:
            return False
        return True
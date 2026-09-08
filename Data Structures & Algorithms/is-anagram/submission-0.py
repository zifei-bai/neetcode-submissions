class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        for char in s:
            hashmap[char] += 1
        
        for char in t:
            hashmap[char] -= 1
        
        for v in hashmap.values():
            if v != 0:
                return False
        
        return True
        
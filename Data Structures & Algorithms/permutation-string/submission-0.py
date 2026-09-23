class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = defaultdict(int)
        for char in s1:
            hashmap[char] += 1
        window_size = len(s1)
        ptr = 0
        for ptr in range(len(s2) - window_size + 1):
            tempmap = defaultdict(int)
            for i in range(ptr, ptr + window_size):
                tempmap[s2[i]] += 1
            if tempmap == hashmap:
                return True
        
        return False
            
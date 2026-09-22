class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        curr_long = 0
        char_count = defaultdict(int)
        char_count[s[0]] += 1

        if len(s) == 1:
            return 1

        for right in range(1, len(s)):
            char_count[s[right]] += 1
            highest_key = max(char_count, key=char_count.get)
            while right - char_count[highest_key] - left + 1 > k:
                char_count[s[left]] -= 1
                left += 1
                highest_key = max(char_count, key=char_count.get)
            curr_long = max(curr_long, right - left + 1)

        return curr_long

    



            
            

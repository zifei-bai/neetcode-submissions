class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        seen = set()
        curr_max = 0
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                curr_max = max(curr_max, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        return curr_max
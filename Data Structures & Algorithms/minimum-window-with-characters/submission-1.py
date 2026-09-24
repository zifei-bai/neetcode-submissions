class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        need = Counter(t)               # 每个字符需要多少个
        window = defaultdict(int)        # 当前窗口里有多少个
        required = len(need)             # 需要满足多少种字符
        formed = 0                       # 已经满足多少种字符

        left = 0
        best_len = float("inf")
        best_start = 0

        for right, char in enumerate(s):
            window[char] += 1

            # 这个字符的数量刚好达到要求
            if char in need and window[char] == need[char]:
                formed += 1

            # 窗口有效：尝试从左边缩小
            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                left_char = s[left]
                window[left_char] -= 1

                # 移走这个字符后，窗口不再满足要求
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]
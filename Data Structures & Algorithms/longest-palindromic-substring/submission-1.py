class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len = 1
        res_start = 0
        for i, x in enumerate(s):
            extend_left = i - 1
            extend_right = i + 1
            curr_i = i
            is_odd = False
            is_even = False

            if 0 <= (extend_left) < (extend_right) < len(s):
                if s[extend_left] == s[extend_right]:
                    is_odd = True
            if 0 <= (curr_i) < (extend_right) < len(s):
                if s[i] == s[extend_right]:
                    is_even = True

            if not is_odd and not is_even:
                continue

            temp_len_odd = 1
            temp_start_odd = i
            if is_odd:
                while 0 <= (extend_left) < (extend_right) < len(s):
                    if s[extend_left] == s[extend_right]:
                        temp_len_odd += 2
                        temp_start_odd = extend_left
                        extend_left -= 1
                        extend_right += 1
                    else:
                        break

            temp_len_even = 0
            temp_start_even = i
            if is_even:
                extend_right = i + 1
                while 0 <= (curr_i) < (extend_right) < len(s):
                    if is_even and s[curr_i] == s[extend_right]:
                        temp_len_even += 2
                        temp_start_even = curr_i
                        curr_i -= 1
                        extend_right += 1
                    else:
                        break

            temp_len = None
            temp_start = None
            if temp_len_odd > temp_len_even:
                temp_len = temp_len_odd
                temp_start = temp_start_odd
            else:
                temp_len = temp_len_even
                temp_start = temp_start_even
            
            if temp_len > res_len:
                res_len = temp_len
                res_start = temp_start
        
        return s[res_start: res_start + res_len]
            



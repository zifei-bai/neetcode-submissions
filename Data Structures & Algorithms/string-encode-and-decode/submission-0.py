class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            length = len(s)
            encoded += f'{length}#{s}'
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            j = i
            while s[j].isdigit() and s[j+1] != '#':
                j += 1
            s_length = int(s[i:j+1])
            s_start = j + 2
            s_end = s_start + s_length
            decoded.append(s[s_start:s_end])
            i = s_end
        return decoded


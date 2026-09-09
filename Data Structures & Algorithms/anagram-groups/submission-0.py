class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        hashmap = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            sorted_strs.append(sorted_s)

        for i, s in enumerate(sorted_strs):
            hashmap[s].append(strs[i])
        ans = []
        for v in hashmap.values():
            ans.append(v)
        return ans

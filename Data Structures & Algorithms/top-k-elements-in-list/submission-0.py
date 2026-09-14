class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for x in nums:
            hashmap[x] += 1
        sorted_dict = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        keys = list(sorted_dict.keys())
        return keys[:k]
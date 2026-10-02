class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-s for s in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            neg_s1 = heapq.heappop(neg_stones)
            neg_s2 = heapq.heappop(neg_stones)
            if neg_s1 == neg_s2:
                continue
            else:
                s1 = -neg_s1
                s2 = -neg_s2

                if s1 < s2:
                    neg_new_s = -(s2 - s1)
                else:
                    neg_new_s = -(s1 - s2)
                
                heapq.heappush(neg_stones, neg_new_s)
                
        if len(neg_stones) == 0:
            return 0
        return -neg_stones[0]
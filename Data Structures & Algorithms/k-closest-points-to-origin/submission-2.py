class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            neg_dist = -dist
            if len(max_heap) < k:
                heapq.heappush(max_heap, (neg_dist, [x, y]))
            else:
                curr_max = -max_heap[0][0]
                if dist < curr_max:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (neg_dist, [x, y]))

        k_points = list(max_heap)

        ans = []
        for elt in k_points:
            ans.append(elt[1])
        
        return ans
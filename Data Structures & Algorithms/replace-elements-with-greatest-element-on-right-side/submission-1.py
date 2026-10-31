class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = deque()
        curr_max = -1
        for i in range(len(arr) - 1, -1, -1):
            ans.appendleft(curr_max)
            curr_max = max(arr[i], curr_max)
        return list(ans)
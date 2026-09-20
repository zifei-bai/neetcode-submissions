class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        water = 0
        prefix[0] = height[0]
        suffix[-1] = height[-1]
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i])
        for j in range(len(height) - 2, -1, -1):
            suffix[j] = max(suffix[j+1], height[j])
        for k in range(len(height)):
            water += min(prefix[k], suffix[k]) - height[k]
        return water
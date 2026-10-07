class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1
        curr_min = float("inf")
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                curr_min = min(curr_min, nums[mid])
                right = mid - 1    
            else:
                curr_min = min(curr_min, nums[left])
                left = mid + 1
            
            
        return curr_min    
            
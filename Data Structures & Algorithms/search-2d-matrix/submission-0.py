class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        oned = []
        for r in range(rows):
            oned += matrix[r]
        left = 0
        right = len(oned) - 1
        while left <= right:
            mid = (left + right) // 2
            if oned[mid] == target:
                return True
            if oned[mid] > target:
                right = mid - 1
            if oned[mid] < target:
                left = mid + 1
        return False


        

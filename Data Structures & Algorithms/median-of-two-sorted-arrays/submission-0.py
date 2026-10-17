class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        left, right = 0, len(A) - 1

        while True:
            amid = (left + right) // 2

            bmid = half - amid - 2

            aleft = A[amid] if amid >= 0 else float('-inf')
            aright = A[amid + 1] if (amid + 1) <= len(A) - 1 else float('inf')
            bleft = B[bmid] if bmid >= 0 else float('-inf')
            bright = B[bmid + 1] if (bmid + 1) <= len(B) - 1 else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2 == 1:
                    return min(aright, bright)
                else:
                    return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                right = amid - 1
            else:
                left = amid + 1

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A  # Ensure A is the shorter array

        total = len(A) + len(B)
        half = total // 2
        
        # 1. Start r at len(A), not len(A)-1, to allow the cut to be AFTER the last element
        l, r = 0, len(A)
        
        while l <= r: # 2. Use <= to ensure we check the final possible cut position
            i = (l + r) // 2  # Cut in A
            j = half - i      # Cut in B
            
            # Boundary values
            # i is the index of the first element in the RIGHT half of A
            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < len(A) else float("inf")
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < len(B) else float("inf")

            # 3. Check if partition is correct
            if A_left <= B_right and B_left <= A_right:
                # Odd total length
                if total % 2:
                    return min(A_right, B_right)
                # Even total length
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1

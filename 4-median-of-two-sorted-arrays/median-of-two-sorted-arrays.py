class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i
            
            left_max1 = float('-inf') if i == 0 else nums1[i-1]
            right_min1 = float('inf') if i == m else nums1[i]
            
            left_max2 = float('-inf') if j == 0 else nums2[j-1]
            right_min2 = float('inf') if j == n else nums2[j]
            
            if left_max1 <= right_min2 and left_max2 <= right_min1:
                # Correct partition found
                if (m + n) % 2 == 0:
                    return (max(left_max1, left_max2) + min(right_min1, right_min2)) / 2
                else:
                    return max(left_max1, left_max2)
            elif left_max1 > right_min2:
                high = i - 1
            else:
                low = i + 1

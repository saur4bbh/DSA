class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        half = (m + n + 1) // 2

        l, r = 0, m # no. of ele from smaller array in final array

        left = right = 0 # both mid of final array

        while l <= r:
            mid = (l + r) // 2
            mid2 = half - mid

            r1 = r2 = float('inf')
            l1 = l2 = float('-inf')

            if mid < m: r1 = nums1[mid]
            if mid-1 >= 0: l1 = nums1[mid-1]
            if mid2 < n: r2 = nums2[mid2]
            if mid2-1 >= 0: l2 = nums2[mid2-1]

            if l1 <= r2 and l2 <= r1:
                left = max(l1, l2)
                right = min(r1, r2)
                break

            elif l2 > r1:
                l = mid + 1

            else:
                r = mid - 1
        
        if (m + n) % 2 == 0:
            return (left + right) / 2
        else:
            return left
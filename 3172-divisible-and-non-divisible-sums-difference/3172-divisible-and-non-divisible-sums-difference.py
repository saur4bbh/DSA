class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1 = n * (n+1) // 2
        nums2 = m * (n//m) * (n//m +1)
        
        return nums1 - nums2
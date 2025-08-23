class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = m+n-1
        i = m-1
        j = n-1

        while j>=0:
            if i>=0 and nums2[j] < nums1[i]:
                nums1[x] = nums1[i]
                i -= 1
            else:
                nums1[x] = nums2[j]
                j -= 1
            x -= 1


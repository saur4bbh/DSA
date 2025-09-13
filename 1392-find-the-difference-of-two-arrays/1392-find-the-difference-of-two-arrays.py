class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        t1 = set(nums1)
        t2 = set(nums2)

        return [ list(t1 - t2) , list(t2 - t1) ]
        
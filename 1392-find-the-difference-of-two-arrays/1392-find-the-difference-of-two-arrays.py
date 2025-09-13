class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        t1 = set(nums1)
        t2 = set(nums2)
        ans = [[],[]]

        for i in t1:
            if i not in t2:
                ans[0].append(i)
        
        for i in t2:
            if i not in t1:
                ans[1].append(i)
        
        return ans
        
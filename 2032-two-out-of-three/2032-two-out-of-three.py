class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        arr = [0] * 101

        for i in nums1:
            arr[i] = 1

        for i in nums2:
            if arr[i] == 1 or arr[i] == 2:
                arr[i] = 2
            else:
                arr[i] = 11

        for i in nums3:
            if arr[i] == 1 or arr[i] == 11:
                arr[i] = 2
        
        ans = []
        for i,val in enumerate(arr):
            if val == 2:
                ans.append(i)
        
        return ans

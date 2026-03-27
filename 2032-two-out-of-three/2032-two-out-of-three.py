class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        arr = [0] * 101

        for i in nums1:
            arr[i] = 'Seen1'

        for i in nums2:
            if arr[i] == 'Seen1' or arr[i] == 'Repeated':
                arr[i] = 'Repeated'
            else:
                arr[i] = 'Seen2'

        for i in nums3:
            if arr[i] == 'Seen1' or arr[i] == 'Seen2':
                arr[i] = 'Repeated'
        
        ans = []
        for i,val in enumerate(arr):
            if val == 'Repeated':
                ans.append(i)
        
        return ans

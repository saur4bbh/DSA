class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_ele = max(arr1) + 1
        count = [0] * max_ele

        for ele in arr1:
            count[ele] += 1
        
        i = 0
        for ele in arr2:
            while count[ele]:
                arr1[i] = ele
                count[ele] -= 1
                i += 1
        
        for idx in range(max_ele):
            while count[idx]:
                arr1[i] = idx
                count[idx] -= 1
                i += 1
        
        return arr1
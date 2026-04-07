class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        idx = 0
        count = 0

        for i,row in enumerate(mat):
            curr = row.count(1)
            if curr > count:
                idx = i
                count = curr
        
        return [idx,count]

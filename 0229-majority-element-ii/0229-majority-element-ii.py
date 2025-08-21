class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = len(nums)//3
        ele1, ele2 = None, None
        count1, count2 = 0, 0

        for i in nums:
            if count1 == 0 and i != ele2:
                ele1, count1 = i, 1
            elif count2 == 0 and i != ele1:
                ele2, count2 = i, 1
            elif i == ele1: count1 += 1
            elif i == ele2: count2 += 1
            else: 
                count1 -= 1
                count2 -= 1
        
        ans = []
        cnt1 ,cnt2 = 0,0
        for j in nums:
            if j == ele1: 
                cnt1 += 1
            elif j == ele2: 
                cnt2 += 1
                
        if cnt1 > t: ans.append(ele1)
        if cnt2 > t: ans.append(ele2)
        
        return ans
            


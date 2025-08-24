class Solution:
    def maxProduct(self, nums):
        track = float('-inf')
        pref = suf = 1
        
        for i in range(len(nums)):
            if pref == 0: pref = 1
            if suf == 0: suf = 1
            pref *= nums[i]
            suf *= nums[~i]
            track = max(track, pref, suf)

        return track
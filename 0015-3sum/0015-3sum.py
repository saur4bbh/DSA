class Solution:
    def threeSum(self, nums):
        n = len(nums)
        a = []
        nums.sort()

        for i in range(n):
            if i>0 and nums[i-1]==nums[i]: continue
            j, k = i+1, n-1
            while j<k:
                summ = nums[i]+nums[j]+nums[k]
                if summ > 0: k -= 1
                elif summ < 0: j += 1
                else:
                    a.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j] == nums[j-1]: j += 1
                    while j<k and nums[k] == nums[k+1]: k -= 1

        return a
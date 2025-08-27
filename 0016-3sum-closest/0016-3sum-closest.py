class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]

        for i in range(n):
            l = i+1
            r = n-1

            while l<r:
                summ = nums[i] + nums[l] + nums[r]
                if abs(target - summ) < abs(target - ans):
                        ans = summ

                if summ > target:
                    r -= 1
                elif summ < target:
                    l += 1
                else:
                    return summ

        return ans

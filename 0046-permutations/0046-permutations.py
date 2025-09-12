class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        part = []

        def backtrack():
            if len(part) == n:
                ans.append(part[:])
                return 
            

            for i in range(n):
                if nums[i] != None:

                    temp = nums[i]
                    part.append(temp)
                    nums[i] = None

                    backtrack()
                    
                    nums[i] = temp
                    part.pop()

        backtrack()
        return ans

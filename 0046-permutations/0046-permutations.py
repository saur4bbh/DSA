class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        temp = []

        def backtrack():
            if len(temp) == n:
                ans.append(temp[:])
                return 
            

            for i in range(n):
                if nums[i] != None:
                    val = nums[i]
                    temp.append(val)
                    nums[i] = None

                    backtrack()
                    
                    nums[i] = val
                    temp.pop()

        backtrack()
        return ans

class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = []
        while num != 0:
            nums.append(str(num%10))
            num //= 10
        nums.reverse()
        for i,val in enumerate(nums):
            if val == '6':
                nums[i] = '9'
                break
        return int(''.join(nums))
class Solution:
    def largestOddNumber(self, num: str) -> str:
    
        for n in range(len(num)-1,-1,-1):
            if int(num[n]) % 2 == 1:
                return num[0 : n+1]

        return ''


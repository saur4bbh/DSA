class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 : return False
        og = x
        rev = 0

        while og != 0:
            rev = rev*10 + og%10
            og //= 10
        
        return rev == x
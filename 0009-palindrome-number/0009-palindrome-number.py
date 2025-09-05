class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 : return False
        
        l = []
        while x != 0:
            l.append(x%10)
            x //= 10

        for i in range(len(l)//2):
            if l[i] != l[~i]:
                return False

        return True
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def pal(s,i,j,deleted):
            while i<j:
                if s[i] != s[j]:
                    if deleted: return False
                    return pal(s,i+1,j,True) or pal(s,i,j-1,True)
                else:
                    i += 1
                    j -= 1
            return True

        return pal(s,0,len(s)-1,False)
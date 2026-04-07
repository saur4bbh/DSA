class Solution:
    def checkString(self, s: str) -> bool:
        b = False
        for i in s:
            if i == 'b':
                b = True
            if b and i == 'a':
                return False
            
        return True
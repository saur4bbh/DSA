class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        value = 0
        for i in s:
            value ^= ord(i)
        for i in t:
            value ^= ord(i)
            
        return chr(value)
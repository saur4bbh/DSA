class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        value = 0

        for i in s:
            value ^= ord(i)
        for j in t:
            value ^= ord(j)
            
        return chr(value)
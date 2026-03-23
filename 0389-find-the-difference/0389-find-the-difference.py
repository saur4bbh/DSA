class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        value = 0

        for i in range(len(t)):
            if i < len(t)-1:
                value ^= ord(s[i]) ^ ord(t[i])
            else:
                value ^= ord(t[i])

        return chr(value)
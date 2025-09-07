class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = {'a':0 ,'e':0 ,'i':0 ,'o':0 ,'u':0 }
        conso = [0]*26

        for i in s:
            if i in vowel:
                vowel[i] += 1
            else:
                conso[ord(i) - ord('a')] += 1
        
        return max(vowel.values()) + max(conso)

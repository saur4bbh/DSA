class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        w1 = len(word1)-1
        w2 = len(word2)-1
        i = 0

        while i<=w1 and i<=w2:
            ans.append(word1[i]+word2[i])
            i += 1
        
        while i<=w1:
            ans.append(word1[i])
            i += 1
        
        while i<=w2:
            ans.append(word2[i])
            i += 1

        return ''.join(ans)



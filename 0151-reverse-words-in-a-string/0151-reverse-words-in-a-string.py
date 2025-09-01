class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        idx = -1       

        for i in range(len(s)-1,-1,-1):       # iterating from last to first
            
            if s[i] != ' ' and idx == -1:     # for tracking last index of each word
                idx = i                  

            elif s[i] == ' ' and idx != -1:     # appending the word as soon as any space found
                ans.append(s[i+1:idx+1])
                idx = -1

        if idx != -1:         # dealing with first word if any
            ans.append(s[i:idx+1])

        return ' '.join(ans)
        
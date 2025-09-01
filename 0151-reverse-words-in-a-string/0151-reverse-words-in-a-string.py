class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        idx = -1

        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ' and idx == -1:
                idx = i
            elif s[i] == ' ' and idx != -1:
                ans.append(s[i+1:idx+1])
                idx = -1

            if i == 0 and idx != -1:
                ans.append(s[i:idx+1])

        return ' '.join(ans)
        
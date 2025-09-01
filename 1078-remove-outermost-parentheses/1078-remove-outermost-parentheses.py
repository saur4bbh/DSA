class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        ans = []
        for i in s:
            if i == ')': cnt -= 1  
            if cnt > 0: ans.append(i)
            if i == '(': cnt+=1    
        return ''.join(ans)
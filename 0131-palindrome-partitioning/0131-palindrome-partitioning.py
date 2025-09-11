class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        temp = []

        def palindrome(start, i):
            while start < i:
                if s[start] != s[i]:
                    return False
                start += 1
                i -= 1
            return True


        def backtrack(start = 0):
            if start == n:
                ans.append(temp[:])
                return
            
            for i in range(start, n):
                if palindrome(start, i):
                    subs = s[start : i+1]
                    temp.append(subs)
                    backtrack(i + 1)
                    temp.pop()
                
            
        backtrack()
        return ans

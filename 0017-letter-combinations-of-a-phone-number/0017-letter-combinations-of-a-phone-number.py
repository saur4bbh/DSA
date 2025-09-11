class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}
        
        n = len(digits)
        ans = []
        
        def backtrack(idx, temp):
            if len(temp) == n:
                ans.append(temp)
                return
            
            word = mapp[digits[idx]]

            for w in word:
                backtrack(idx + 1, temp + w)

        backtrack(0, '')
        if digits == '':
            return []
        return ans

            

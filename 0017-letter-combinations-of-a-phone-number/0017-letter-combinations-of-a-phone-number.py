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
        
        def backtrack(i, temp):
            if len(temp) == n:
                ans.append(temp)
                return
            
            val = mapp[digits[i]]

            for letter in val:
                backtrack(i + 1,temp + letter)
        
        backtrack(0, '')
        if digits == '':
            return []
        return ans
        



            

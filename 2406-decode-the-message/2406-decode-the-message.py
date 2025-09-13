class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen = {' ':' '}
        a = 0
        for i in key:
            if i != ' ' and i not in seen:
                seen[i] = chr(a + 97)
                a += 1
        
        return ''.join(seen[i] for i in message)
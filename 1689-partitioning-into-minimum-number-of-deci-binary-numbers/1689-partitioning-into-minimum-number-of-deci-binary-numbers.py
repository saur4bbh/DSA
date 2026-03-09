class Solution:
    def minPartitions(self, n: str) -> int:
        ans = '0'
        for i in n:
            if i == '9': 
                return 9
            ans = max(ans, i)
                
        return int(ans)
        
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [None]*n
        if n%2 != 0:
            ans[-1] = 0

        for i in range(1,n,2):
            ans[i-1] = i
            ans[i] = -i

        return ans
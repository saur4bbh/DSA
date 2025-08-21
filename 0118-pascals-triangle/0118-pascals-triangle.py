class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def row(n):
            ans = 1
            r = [1]
            for i in range(1,n):
                ans = ans * (n - i) // i
                r.append(ans)
            return r

        pascal = []
        for i in range(1,numRows+1):
            pascal.append(row(i))

        return pascal


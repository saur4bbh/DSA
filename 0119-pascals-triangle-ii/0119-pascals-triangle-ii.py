class Solution:
    def getRow(self, r: int) -> List[int]:
        row = [1]

        for i in range(1,r+1):
            row.append(row[-1] * (r + 1 - i) // i)

        return row
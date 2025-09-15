class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def solve(idx, total, temp, lastnum):
            if idx == n:
                if total == target:
                    ans.append(temp)
                return

            for i in range(idx, n):
                if i > idx and num[idx] == '0':
                    break

                currnum_str = num[idx : i+1]
                currnum = int(currnum_str)

                if idx == 0:
                    solve(i + 1, currnum, currnum_str, currnum)
                else:
                    solve(i + 1, total + currnum, temp + '+' + currnum_str, currnum)
                    solve(i + 1, total - currnum, temp + '-' + currnum_str, -currnum)
                    solve(i + 1, total + (lastnum * currnum) - lastnum, temp + '*' + currnum_str, lastnum * currnum)
            
        solve(0, 0, '', 0)
        return ans
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def backtrack(idx: int, total: int, temp: str, prev: int):
            if idx == n:
                if total == target:
                    ans.append(temp)
                return

            for j in range(idx, n):
                # Skip numbers with leading zeros
                if j > idx and num[idx] == '0':
                    break

                last_num_str = num[idx:j+1]
                last_num = int(last_num_str)

                if idx == 0:
                    # First number, no operator
                    backtrack(j+1, last_num, last_num_str, last_num)
                else:
                    # Addition
                    backtrack(j+1, total + last_num, temp + '+' + last_num_str, last_num)
                    # Subtraction
                    backtrack(j+1, total - last_num, temp + '-' + last_num_str, -last_num)
                    # Multiplication
                    backtrack(j+1, total - prev + (prev * last_num), temp + '*' + last_num_str, prev * last_num)

        backtrack(0, 0, '', 0)
        return ans

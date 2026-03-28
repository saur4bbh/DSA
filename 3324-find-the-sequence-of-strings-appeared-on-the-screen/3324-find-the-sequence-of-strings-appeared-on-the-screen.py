class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ele = []
        ans = []

        for alpha in target:
            loop = ord(alpha) - ord('a')
            ele.append('')

            for j in range(loop + 1):
                num = ord('a') + j
                ele[-1] = chr(num)
                ans.append( ''.join(ele) )

        return ans
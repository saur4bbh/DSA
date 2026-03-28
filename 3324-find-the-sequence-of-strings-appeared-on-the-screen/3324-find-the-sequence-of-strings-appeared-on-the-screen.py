class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        ele = ''

        for alpha in target:
            for code in range(ord('a'), ord(alpha) + 1):
                ans.append(ele + chr(code))

            ele += alpha

        return ans
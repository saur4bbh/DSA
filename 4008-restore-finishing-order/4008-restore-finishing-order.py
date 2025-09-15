class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        ids = set(friends)
        for i in order:
            if i in ids:
                ans.append(i)

        return ans

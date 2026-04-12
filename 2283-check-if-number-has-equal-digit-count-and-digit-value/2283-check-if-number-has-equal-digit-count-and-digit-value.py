class Solution:
    def digitCount(self, num: str) -> bool:
        count = defaultdict(int)

        for val in num:
            count[val] += 1
        
        for i,val in enumerate(num):
            if int(val) != count[str(i)]:
                return False

        return True
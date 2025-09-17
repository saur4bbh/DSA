class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(force):  
        # min of max means > than force in def is allowed but not lesser than this
            containers = 1
            temp = 0
            for i in range(1, len(position)):
                temp += position[i] - position[i-1]
                if temp > force:
                    containers += 1
                    temp = 0
                if containers >= m:
                    return True
            return False
        
        l, r = 1, position[-1] - position[0]
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1 
        
        return l
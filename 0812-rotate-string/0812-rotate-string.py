class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            
        idx = 0
        for i in range(len(s)):
            if s[0] == goal[i]:
                if s == goal[i:] + goal[:i]:
                    return True
        return False

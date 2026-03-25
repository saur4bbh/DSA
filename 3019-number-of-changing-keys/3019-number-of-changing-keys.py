class Solution:
    def countKeyChanges(self, s: str) -> int:
        changed = 0
        for i in range(len(s)-1):
            if s[i].lower() != s[i+1].lower():
                changed += 1
        
        return changed
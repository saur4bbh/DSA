class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {'type':0,'color':1,'name':2}
        key = d[ruleKey]
        count = 0
        for i in items:
            if i[key]==ruleValue:
                count+=1
        return count
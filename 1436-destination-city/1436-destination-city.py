class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        citya = set()
        for i in paths:
            citya.add(i[0])

        for i in paths:
            if i[1] not in citya:
                return i[1]
        
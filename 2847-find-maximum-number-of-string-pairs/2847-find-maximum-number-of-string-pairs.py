class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt = 0
        track = set()
        for word in words:
            if word[::-1] in track:
                cnt += 1
            else:
                track.add(word)
        return cnt
        
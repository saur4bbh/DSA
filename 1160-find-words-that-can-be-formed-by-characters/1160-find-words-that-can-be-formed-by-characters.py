class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char = defaultdict(int)
        for c in chars:
            char[c] += 1
        
        ans = 0
        for word in words:
            track = char.copy()
            ans += len(word)
            for w in word:
                if w not in track or track[w] == 0:
                    ans -= len(word)
                    break
                else:
                    track[w] -= 1
        
        return ans
                
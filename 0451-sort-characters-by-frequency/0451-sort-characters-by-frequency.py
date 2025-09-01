class Solution:
    def frequencySort(self, s: str) -> str:
        a = [[0,i] for i in range(123)]
        ans = []
        for i in s:
            if i.isdigit():
                a[int(i)][0] += 1
            else:
                a[ord(i)][0] += 1
        
        a.sort(reverse = True)

        j = 0
        while a[j][0] != 0:
            if a[j][1] < 10:
                for i in range(a[j][0]):
                    ans.append(str(a[j][1]))
            else: 
                for i in range(a[j][0]):
                    ans.append(chr(a[j][1]))
            j += 1

        return ''.join(ans)



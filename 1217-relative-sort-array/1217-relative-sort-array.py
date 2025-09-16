class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        bucket = defaultdict(int)

        for element in arr1:
            bucket[element] += 1

        i = 0
        for element in arr2:
            while bucket[element]:
                arr1[i] = element
                bucket[element] -= 1
                i += 1
        
        temp = []
        for leftover in bucket:
            while bucket[leftover]:
                temp.append(leftover)
                bucket[leftover] -= 1

        j = 0
        temp.sort()
        for element in temp:
            arr1[i] = temp[j]
            i += 1
            j += 1
        
        return arr1

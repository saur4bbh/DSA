class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total = m + n

        mid1 = (m + n - 1) // 2
        mid2 = (m + n) // 2

        ele1 = ele2 = 0

        cnt = 0
        i = j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                ele1, ele2 = nums1[i],ele1
                i += 1
            else:
                ele1, ele2 = nums2[j],ele1
                j += 1

            if cnt == mid2:
                if (m+n) % 2 == 0:
                    return (ele1 + ele2) / 2
                else:
                    return ele1
            cnt += 1

        while i<m:
            ele1, ele2 = nums1[i],ele1
            i += 1
            if cnt == mid2:
                if (m+n) % 2 == 0:
                    return (ele1 + ele2) / 2
                else:
                    return ele1
            cnt += 1

        while j<n:
            ele1, ele2 = nums2[j],ele1
            j += 1
            if cnt == mid2:
                if (m+n) % 2 == 0:
                    return (ele1 + ele2) / 2
                else:
                    return ele1
            cnt += 1
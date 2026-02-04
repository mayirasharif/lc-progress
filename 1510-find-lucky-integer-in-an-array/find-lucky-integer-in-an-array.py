class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter

        hash = Counter(arr)

        sortedArr = sorted(arr)[::-1]
        for num in sortedArr:
            if hash[num] == num:
                return num
        return -1
        
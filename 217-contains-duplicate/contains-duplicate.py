class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # input -> array[ints]
        # output -> boolean

        seen = {}

        # O(n) time complexity

        for n in nums:
            if n in seen:
                return True
            seen[n] = 1
        return False
        
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        # given an integer array nums with nums.length = 2 * n

        # nums contains n + 1 unique elements!

        # exactly one element is repeated n times!

        from collections import Counter

        n = len(nums) // 2

        freqs = Counter(nums)
        print(freqs)

        for key, freq in freqs.items():
            if freq == n:
                return key


        
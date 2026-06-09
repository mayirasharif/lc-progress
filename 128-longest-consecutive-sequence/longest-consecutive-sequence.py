class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorting method -> count increments.

        # sorted_nums = sorted(nums)

        # screw it

        nums = sorted(nums)
        print(nums)

        max_i = 0
        i = 0
        for n in range(len(nums)):
            if n == 0:
                i += 1
                max_i = max(max_i, i)
            elif n < len(nums):
                if nums[n] == 1 + nums[n-1]: 
                    i += 1
                    max_i = max(max_i, i)
                elif nums[n] == nums[n-1]:
                    continue
                else:
                    i = 1
        return max_i






        
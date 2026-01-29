class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

    # given an array of integers

    # return indices of teh two numbers so they add up to target.

        hash = {}
        # this is easy, why is it taking me too long!!!!??

        # forgot how to do this lol

        for x in range(len(nums)):
                if (target - nums[x]) in hash:
                    return [hash[(target - nums[x])], x]
                hash[nums[x]] = x



         
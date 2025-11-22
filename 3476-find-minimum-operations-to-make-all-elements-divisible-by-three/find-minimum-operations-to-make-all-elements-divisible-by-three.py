class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            # check if num - rem or num + rem is needed
            
            if nums[i] % 3 == 0:
                continue
            result += 1
        return result
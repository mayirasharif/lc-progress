class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        times = 0
        while sum(nums) % k != 0:
            nums[0] -= 1
            times += 1
        return times

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # first case - nums sum to 0
        
        for i in range(len(nums)):

            sumleft = sum(nums[:i])
            sumright = sum(nums[i+1:])
            print(sumleft, sumright)
            if sumleft == sumright:
                return i
        return -1



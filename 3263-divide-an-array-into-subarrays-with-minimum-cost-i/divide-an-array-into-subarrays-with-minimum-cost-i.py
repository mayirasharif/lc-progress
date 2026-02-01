class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        """
        # brute force -> sort solution

        sortedNums = sorted(nums)

        # form the subarrays/total

        # we're only taking the 1st value of each
        # and first 2 array lengths dont matter

        # to optimize, we just want each of the three arrays to have the lowest FIRST value possible

        
        update: cannot sort
        """
        sortedNums = sorted(nums)

        smallestNums = sortedNums[:2]
        print(smallestNums)

        # hmm. include the first val, then split based on encountering one of the 3 smallest nums
        total = 0
        arr = 0
        i = 0
        
        sortedNums = sorted(nums[1:])

        return nums[0] + sortedNums[0] + sortedNums[1]
        

            





       
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # linear runtime complexity
        # constant space - aka no hashmaps, etc.

        res = 0
        for num in nums:
            res = num ^ res
            print(res, num)
        return res
        

        

        
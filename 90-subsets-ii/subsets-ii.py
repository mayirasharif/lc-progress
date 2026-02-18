class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # we want to find all the subsets of our set.

        # so we want to use a backtracking approach here, without duplicates.

        # how do i remove duplicates? i don't know.
        theSet = [[]]
        n = len(nums) - 1
        def backtrack(i, subset=[]): # we use an integer increment for space complexity reduction
            if i > n:
                if sorted(subset) not in theSet:
                    theSet.append(sorted(subset))
                return
            
            backtrack(i+1, subset)
            backtrack(i+1, subset + [nums[i]])

        backtrack(0)

        return theSet

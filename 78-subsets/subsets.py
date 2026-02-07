class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking problem

        # given: integer array nums
        # return: all possible subsets

        # no duplicates (simple enough)

        # basic backtracking formula
        res = []
        subset = []

        n = len(nums)
        def backtrack(i):
            """
            append all combinations into res

            start -> n possibilities
            next run -> n - 1 possibilities
            ...
            final run -> 1 choice

            [1, 2, 3]

            [1] -> stop
            [1, 2] -> stop
            [1, 2, 3] -> stop

            [2] -> stop
            [2, 3] -> stop

            [2, 1] -> stop (duplicate) -> how tell?
            """
            if i >= n:
                res.append(subset.copy())
            else:
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
                backtrack(i+1)
            return
        backtrack(0)
        return res

            # i dunno how to start here.
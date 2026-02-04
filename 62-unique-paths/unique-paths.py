class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # gonna go ahead and redo this just to see if i remember

        # no mic so just gonna have to type stuff

        # this is a classic dynamic programming problem here
        # the idea is that you have to sum up the total "possibilities"
        # and keep track of "mini-solutions" you encounter along the way

        memo = {} # we use a hashmap to..... uhhh, i think it was a hashmap?
        # regardless lets continue

        # you need a recursive dp function like this:
        def dp(i, j):
            # here you have multiple cases:
            if (i, j) in memo:
                return memo[(i, j)]

            # the best case ( we made it )
            if (i, j) == (m - 1, n - 1):
                return 1
            
            # the out of bounds case (where the robot goes beyond bounds)
            if i >= m or j >= n or i < 0 or j < 0:
                return 0
            
            # now for our recursive call: the purpose of this is to get the sum total of "paths" towards the bottom-right from THIS SPECIFIC location
            res = dp(i + 1, j) + dp(i, j + 1)
            memo[(i, j)] = res



            return res
        
        # it says we start at grid[0][0]. so before we do anything....
        return dp(0, 0)

        # good! time limit exceeded. means we NEED to use memoization.
        # but how?             
        
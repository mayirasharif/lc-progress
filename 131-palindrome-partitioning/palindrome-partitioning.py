class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start, path):
            # Base case: we've used the whole string
            if start == n:
                res.append(path.copy())
                return
            
            # Try every possible substring starting at `start`
            for end in range(start, n):
                if isPalindrome(start, end):
                    # Choose
                    path.append(s[start:end+1])
                    
                    # Explore
                    backtrack(end + 1, path)
                    
                    # Un-choose
                    path.pop()

        backtrack(0, [])

        """
        ⚡ The Key Difference
        Combination Sum:

        Constraint applies to the entire finished structure (sum == target).

        Palindrome Partition:

        Constraint applies to every individual piece as you build it.
"""

        return res
                
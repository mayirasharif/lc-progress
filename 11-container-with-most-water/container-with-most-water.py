class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height) - 1
        l = 0

        # two pointer problem, best case is when the l and r points are farthest away, but when their heights are highest....
        # how would I determine when to move the l and r points?

        # i could eliminate heights BIGGER than itself--since the area will be determined by itself-- thus it would be height * distance.

        squares = 0

        #GAMEPLAN: Use the hints \U0001f92a to find out to move the pointer with the lower height.

        while l < r:
            if height[l] > height[r]:
                area = ((r-l)*height[r])
                squares = max(area, squares)
                r -= 1
            else:
                area = ((r-l)*height[l])
                squares = max(area, squares)
                l += 1

        return squares


        
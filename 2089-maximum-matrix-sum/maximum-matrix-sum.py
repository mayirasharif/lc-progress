class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        # goal: maximized the summation of matrix's elements
        # return the max sum of the matrix's elements - choose two
        
        # can do this operation any number of times....

        # Until what condition(s) are met?

        # Ex 1: [[1, -1], [-1, 1]] -> sum = 4, 2 times
        # Ex 2: [[1, 2, 3], [-1, -2, -3], [1, 2, 3]] -> sum = 16, 1 time

            # why stop after 1? 1 is smallest val, any swap further would either be redundant (say 1 and 1) or detrimental (-1 and 2 or 3)

        
        def findAbsSum(matrix):
            sum = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    sum += abs(matrix[i][j])
            return sum
        

        def findSum(matrix):
            sum = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    sum += matrix[i][j]
            return sum
        
        def turnPositive(matrix):
            minNum = float('inf')
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    minNum = min(minNum, abs(matrix[i][j]))
                    matrix[i][j] = abs(matrix[i][j])

            
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if abs(matrix[i][j]) == minNum:
                        matrix[i][j] = -(matrix[i][j])
                        return

            return



        """
        for r in range(len(matrix)):
            for c in range(len(matrix[0]) - 1):

                if matrix[r][c] < 0:
                    if matrix[r][c+1] < 0:
                        matrix[r][c] = -(matrix[r][c])
                        matrix[r][c+1] = -(matrix[r][c+1])
        
        print(matrix)
            
        """

        # what if.....

        def numNegative(matrix):
            numNeg = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] < 0:
                        numNeg += 1
            return numNeg


        if numNegative(matrix) % 2 == 0:
            return findAbsSum(matrix)
        else:
            minVal = turnPositive(matrix)
            return findSum(matrix)




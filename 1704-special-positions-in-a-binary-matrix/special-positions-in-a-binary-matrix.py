class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        def row_col_check(i, j):
            row_sum = 0
            # check row i
            for c in range(len(mat[i])):
                row_sum += mat[i][c]
            if row_sum > 1:
                return 0
            
            # check col j
            col_sum = 0
            for r in range(len(mat)):
                col_sum += mat[r][j]
            if col_sum > 1:
                return 0
            return 1
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    res += row_col_check(i, j)
        return res

            
        
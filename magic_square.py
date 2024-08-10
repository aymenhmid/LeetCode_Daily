# problem link : https://leetcode.com/problems/magic-squares-in-grid/?envType=daily-question&envId=2024-08-09
class Solution(object):
    @staticmethod
    def count_elements(matrix):
        element_count = {}
        
        for row in matrix:
            for element in row:
                if element in element_count:
                    element_count[element] += 1
                else:
                    element_count[element] = 1
        
        return element_count
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)       # Number of rows in the matrix
        m = len(grid[0]) 
        submatrices = []
    
        # Iterate over possible starting rows
        count = 0
        
        if n >=3 and m >=3:
            for i in range(n - 2):
                # Iterate over possible starting columns
                for j in range(m - 2):
                    # Extract the 3x3 submatrix
                    submatrix = [row[j:j+3] for row in grid[i:i+3]]
                    #print(submatrix)
                    submatrices.append(submatrix)
        for submatrix in submatrices:
            lst = self.count_elements(submatrix).values()
            lst2 = self.count_elements(submatrix).keys()
            s1 = sum(submatrix[0])
            s2 = sum(submatrix[1])
            s3 = sum(submatrix[2])
            s4 = submatrix[0][0] + submatrix[1][0] + submatrix[2][0]
            s5 = submatrix[0][1] + submatrix[1][1] + submatrix[2][1]
            s6 = submatrix[0][2] + submatrix[1][2] + submatrix[2][2]
            s7 = submatrix[0][0] + submatrix[1][1] + submatrix[2][2]
            s8 = submatrix[0][2] + submatrix[1][1] + submatrix[2][0]
            if s1 == s2 == s3 == s4 == s5 == s6 == s7 == s8 and all(x == 1  for x in lst) and all(1 <= x <= 9  for x in lst2):
                count+=1
        return count
        

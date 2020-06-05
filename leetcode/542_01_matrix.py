class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    top = matrix[i - 1][j] if i else float('inf')
                    left = matrix[i][j - 1] if j else float('inf')
                    matrix[i][j] = min(top, left) + 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j]:
                    bottom = matrix[i + 1][j] if i < m - 1 else float('inf')
                    right = matrix[i][j + 1] if j < n - 1 else float('inf')
                    matrix[i][j] = min(matrix[i][j], bottom + 1, right + 1)
        return matrix

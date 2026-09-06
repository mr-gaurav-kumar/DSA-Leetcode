class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        result = [[0] * c for _ in range(r)]

        for i in range(m * n):
            result[i // c][i % c] = mat[i // n][i % n]

        return result


# Time: O(m × n)
# Auxiliary space: O(1)
# Output space: O(r × c)
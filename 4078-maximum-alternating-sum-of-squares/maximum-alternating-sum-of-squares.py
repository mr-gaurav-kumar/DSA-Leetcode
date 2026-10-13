
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted((num * num for num in nums), reverse=True)

        positive = 0
        negative = 0

        for i, value in enumerate(squares):
            if i < (len(squares) + 1) // 2:
                positive += value
            else:
                negative += value

        return positive - negative


# Time COmplexity = O(n log n)
# Space Complexity = O(n)

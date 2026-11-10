
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):

            for jump in range(1, 4):

                j = i + jump

                if j <= n:
                    current_cost = costs[j - 1] + jump ** 2

                    dp[j] = min(
                        dp[j],
                        dp[i] + current_cost
                    )

        return dp[n]
# Time Complexity: O(n))
# Space Complexity: (O(n))
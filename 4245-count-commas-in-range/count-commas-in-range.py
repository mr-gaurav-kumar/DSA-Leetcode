class Solution:
    def countCommas(self, n: int) -> int:
        total = 0

        for i in range(1, n+1):
            # count = 0
            if  i >= 1000:

                # count = count + 1

                total = total + 1

        return total


# Time Complexity = O(n)
# Space Complexity = O(1)
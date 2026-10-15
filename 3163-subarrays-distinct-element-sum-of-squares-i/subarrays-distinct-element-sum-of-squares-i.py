class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        full = 0

        for _ in range(n):
            s = set()

            for __ in range (_,n):
                s.add(nums[__])
                full = full + len(s) ** 2

        return full

# Time Complexity = O(n^2)
# Space Complexity = O(n)
        
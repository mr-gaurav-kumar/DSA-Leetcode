class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller = sum(1 for x in nums if x < target)
        count = nums.count(target)

        return list(range(smaller, smaller + count))


# TC = (O(n))
# Auxiliary SC = (O(1))
# Output Space = (O(k)
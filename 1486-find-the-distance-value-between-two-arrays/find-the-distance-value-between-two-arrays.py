class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:

        count = 0

        for i in range(len(arr1)):
            valid = True

            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count

# Time Complexity: O(n × m)
# Space Complexity: O(1)
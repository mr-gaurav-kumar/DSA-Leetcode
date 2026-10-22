
from typing import List
from collections import deque

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Determine the cyclic direction
        if all(nums[i] == (nums[0] + i) % n for i in range(n)):
            direction = 1
        elif all(nums[i] == (nums[0] - i) % n for i in range(n)):
            direction = -1
        else:
            return -1

        # State: (first element, direction)
        start = (nums[0], direction)
        target = (0, 1)

        queue = deque([(start[0], start[1], 0)])
        visited = {start}

        while queue:
            k, d, steps = queue.popleft()

            if (k, d) == target:
                return steps

            # Operation 1: Rotate left by one
            state1 = ((k + d) % n, d)
            if state1 not in visited:
                visited.add(state1)
                queue.append((state1[0], state1[1], steps + 1))

            # Operation 2: Reverse the entire array
            state2 = ((k - d) % n, -d)
            if state2 not in visited:
                visited.add(state2)
                queue.append((state2[0], state2[1], steps + 1))

        return -1


# Time complexity = O(n)
# Space Complexity = O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for a in s:
            if a in "({[":
                stack.append(a)
            else:
                if not stack or stack.pop() != pairs[a]:
                    return False

        return not stack


# Time Complexity = O(n)
# Space Complexity = O(n)
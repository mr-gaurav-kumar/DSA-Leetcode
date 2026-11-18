class Solution:
    def minChanges(self, s: str) -> int:
        count = 0

        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                count = count + 1
        return count

# Time COmplexity = O(n)
# Spcae Complexity = O(1)
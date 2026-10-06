class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        ans = 0

        for ch in s:
            if ch == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    ans += 1

        ans += balance

        return ans

# Time: O(n)
# Space: O(1)
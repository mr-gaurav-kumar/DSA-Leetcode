class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        alice_turn = True

        while n >= stones:
            n = n -stones
            stones = stones - 1
            alice_turn = not alice_turn

        return not alice_turn

# Time Complexity = O(1)
# Space Complexity = O(1)
        
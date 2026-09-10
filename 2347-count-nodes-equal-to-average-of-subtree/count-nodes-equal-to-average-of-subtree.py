# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def get_sum_count(node):
            if node is None:
                return 0, 0

            left_sum, left_count = get_sum_count(node.left)
            right_sum, right_count = get_sum_count(node.right)

            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            return total_sum, total_count

        def traverse(node):
            if node is None:
                return 0

            total_sum, total_count = get_sum_count(node)

            average = total_sum // total_count

            count = 0

            if node.val == average:
                count += 1

            count += traverse(node.left)
            count += traverse(node.right)

            return count

        return traverse(root)


# Time Complexity = O(n²)
# Space Complexity = O(n)
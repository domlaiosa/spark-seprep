class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        median = (len(nums) // 2)
        left_tree = nums[:median]
        right_tree = nums[median+1:]
        new = TreeNode(nums[median])
        new.left = Solution.sortedArrayToBST(self, left_tree)
        new.right = Solution.sortedArrayToBST(self, right_tree)
        return new


## Test Case
nums  = [-19, -10, -7, 0, 4, 17, 53, 57, 59, 60, 61]
Sol = Solution()
sorted = Sol.sortedArrayToBST(nums)
print(f'The resulting tree for {nums} is {sorted}')
print("If you're reaidng this far yes I know thats just a pointer but I don't think adding code for tree parsing is necessary for this assignment. My solution passes on leetcode :)")
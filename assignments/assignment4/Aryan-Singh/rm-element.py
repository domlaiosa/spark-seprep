class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        sum=0
        while val in nums:
                nums.remove(val)
        nums

def test_remove_element():
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    expected_output = [2, 2]
    
    # Call the removeElement method
    solution.removeElement(nums, val)
    
    # Check if the modified array matches the expected output
    assert nums == expected_output, f"Expected {expected_output}, but got {nums}"
    
    print("Test passed!")

# Run the test
test_remove_element()

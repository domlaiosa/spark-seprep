# LeetCode Problem: Remove Duplicates from Sorted Array
# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#
# Given an integer array nums sorted in non-decreasing order, remove the duplicates 
# in-place such that each unique element appears only once. The relative order of 
# the elements should be kept the same. Return k after placing the final result in 
# the first k slots of nums.
#
# Example:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

def removeDuplicates(nums):
    count = 0
    while count < len(nums) - 1:  # Make sure next_index doesn't go out of bounds
        next_index = count + 1
        if nums[next_index] == nums[count]:
            del nums[next_index]  # Remove the duplicate element
        else:
            count += 1  # Only move to the next index if no deletion occurs
    return len(nums)

# Test case
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeDuplicates(nums)
print(f"Updated list with unique elements: {nums[:k]}")
print(f"Number of unique elements: {k}")

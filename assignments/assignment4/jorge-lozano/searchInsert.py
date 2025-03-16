#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:08:36 2024

@author: jorge
"""



def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2  
            
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1 
            else:
                right = middle - 1  
        
        return left


nums = [1, 3, 5, 6]
target = 5
result = searchInsert(nums, target)
print(f"The index of {target}: {result}")
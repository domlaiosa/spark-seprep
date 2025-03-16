class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                # If the digit is less than 9, just increment it and return the array
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0
            digits[i] = 0
        
        # If all digits were 9 (e.g., 999 -> 1000)
        return [1] + digits

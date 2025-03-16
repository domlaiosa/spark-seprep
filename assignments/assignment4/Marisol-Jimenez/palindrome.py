# Given an integer x, return true if x is a palindrome, and false otherwise.

# Question: Given an array of integers nums return False if the list is not a palindrome. R
# Return True otherwise

# Eample arr = [1,4, 3, 4, 5] will return True and arr = [1, 4, 3, 3, 1] will return
# False

def is_palindrome(arr):
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - 1 - i]:
            print("False")
            return False
    return True

## Test case
arr = [1, 4, 3, 4, 1]
x= is_palindrome(arr)
print("This arry is a palindrome:"+ str(x))

def isPalindrome(x):
    if x < 0:
        return False

    reverse = 0
    xcopy = x

    while x > 0:
        reverse = (reverse * 10) + (x % 10)
        x //= 10
    
    return reverse == xcopy

# test case
print(isPalindrome(515))  # true
print(isPalindrome(123456))  # false
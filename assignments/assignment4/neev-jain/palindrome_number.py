def isPalindrome(x):
    if x < 0:
        return False
    if x == 0:
        return True
    if x % 10 == 0:
        return False

    numReversed = 0
    originalNumber = x

    while originalNumber > 0:
        lastDigit = originalNumber % 10
        numReversed = numReversed*10+lastDigit
        originalNumber = originalNumber//10

    return x == numReversed


# Test Cases
print(isPalindrome(121))  # True
print(isPalindrome(-121))  # False
print(isPalindrome(10))  # False

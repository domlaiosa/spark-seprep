def isPalindrome(x):
    x = str(x)
    for i in range(len(x)):
        if x[i] != x[len(x)-i-1]:
            return False

    return True


x = 12121
result = isPalindrome(x)
print(f'Is {x} a palindrome number? {result}')
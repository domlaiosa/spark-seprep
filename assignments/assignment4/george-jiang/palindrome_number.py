def is_palindrome(x):
    # Convert the number to a string to check if it reads the same backward
    return str(x) == str(x)[::-1]

# Test case
x = 121
result = is_palindrome(x)
print(f"Is {x} a palindrome? {result}")


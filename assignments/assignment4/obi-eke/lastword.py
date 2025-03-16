class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        if not words:
            return 0
        return len(words[-1])

# Test case
solution = Solution()
s = "Hello World"
result = solution.lengthOfLastWord(s)
print{f"The length of the last word in 'Hello World' is {result}")

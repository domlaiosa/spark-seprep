class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        diff_sum = 0
    
    # Iterate over each character in s
        for char in s:
            index_s = s.index(char)  # index of char in s
            index_t = t.index(char)  # index of char in t
            diff_sum += abs(index_s - index_t)  # add the absolute difference
    
        return diff_sum

# Test Case 1: Identical strings
s = "abcd"
t = "abcd"
print(permutation_difference(s, t))  # Output should be 0

# Test Case 2: Reversed string
s = "abcd"
t = "dcba"
print(permutation_difference(s, t))  # Output should be 8

class Solution(object):
    def lengthOfLastWord(self, s):
        cleaned_string =' '.join(s.split())
        seperated = cleaned_string.split(' ')
        last_word = seperated[-1]
        return len(last_word)

s = Solution()
words ='Hello World'
result = s.lengthOfLastWord(words)

print(result)
def isSubsequence(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sub = 0
        tot = 0
        if s == "":
            return True

        while(tot < len(t) and sub < len(s)):
            if t[tot] == s[sub]:
                if sub == len(s) -1:
                    return True
                tot += 1
                sub += 1
            else:
                tot += 1
        return False

# Test Case
s = 'abc'
t = 'ahellobgoodbyec'
result = isSubsequence(s, t)
print('Valid Subsequence: ', result)

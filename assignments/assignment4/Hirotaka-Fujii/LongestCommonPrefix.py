class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or strs[0] == "":
            return ""
        fin = ""
        matches = True
        prev = strs[0][0]
        for i in range(len(strs)):
            if strs[i] == "":
                return ""
            if strs[i][0] != prev:
                matches = False
            strs[i] = strs[i][1:]
        if matches:
            fin +=  prev + self.longestCommonPrefix(strs)
        return fin

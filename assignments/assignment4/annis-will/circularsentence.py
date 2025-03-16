class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        ss = sentence.split()
        n = len(ss)
        return all(s[-1] == ss[(i + 1) % n][0] for i, s in enumerate(ss))
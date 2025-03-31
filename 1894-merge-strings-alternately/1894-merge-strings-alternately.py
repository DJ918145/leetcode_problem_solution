class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ""
        # min_len = min(len(word1), len(word2))
        for i in range(min(len(word1), len(word2))):
            res += word1[i] + word2[i]
        if len(word1) == len(word2):
            return res
        elif len(word2)>len(word1):
            res += word2[min(len(word1), len(word2)):]
        else:
            res += word1[min(len(word1), len(word2)):]
        return res
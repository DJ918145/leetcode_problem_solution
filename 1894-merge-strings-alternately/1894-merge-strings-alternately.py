class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ""
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            res += word1[i] + word2[i]
        if len(word1) == len(word2):
            return res
        elif len(word2)>len(word1):
            res += word2[min_len:]
        else:
            res += word1[min_len:]
        return res
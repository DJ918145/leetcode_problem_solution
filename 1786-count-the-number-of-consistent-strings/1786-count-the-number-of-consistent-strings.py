class Solution(object):
    def countConsistentStrings(self, allowed, words):
        size = len(words)
        count = 0
        for i in range(size):
            word = words[i]
            size2 = len(word)
            for j in range(size2):
                if word[j] in allowed:
                    if j == size2-1:
                        count = count +1
                    else:
                        pass
                else:
                    break
        return count
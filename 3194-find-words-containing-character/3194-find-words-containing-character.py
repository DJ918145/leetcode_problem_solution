class Solution(object):
    def findWordsContaining(self, words, x):
        answer = []
        for index in range(len(words)):
            if x in words[index]:
                answer.append(index)
        return answer        
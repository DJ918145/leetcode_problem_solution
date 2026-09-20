class Solution(object):
    def topKFrequent(self, words, k):

        word_dict = {}

        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

        sorted_words = sorted(
            word_dict.items(),
            key=lambda x: (-x[1], x[0])
        )

        return [word for word, count in sorted_words[:k]]
class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            # Sort the word manually (without using sorted or imports)
            key = self.sortWord(word)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())

    def sortWord(self, word):
        # Convert string to list of characters and implement simple bubble sort
        chars = list(word)
        n = len(chars)
        for i in range(n):
            for j in range(0, n - i - 1):
                if chars[j] > chars[j + 1]:
                    chars[j], chars[j + 1] = chars[j + 1], chars[j]
        return ''.join(chars)
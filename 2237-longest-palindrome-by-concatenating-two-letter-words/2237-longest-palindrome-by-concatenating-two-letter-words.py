from collections import Counter

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        freq = Counter(words)
        count = 0
        central_used = False
        
        for word in list(freq.keys()):
            rev = word[::-1]
            if word != rev:
                # Match non-palindromic word with its reverse
                if rev in freq:
                    pairs = min(freq[word], freq[rev])
                    count += pairs * 4
                    freq[word] -= pairs
                    freq[rev] -= pairs
            else:
                # Word is a palindrome itself like "gg"
                pairs = freq[word] // 2
                count += pairs * 4
                freq[word] -= pairs * 2

        # After pairing, check if we can use one palindromic word in the center
        for word in freq:
            if word[0] == word[1] and freq[word] > 0:
                count += 2
                break
        
        return count

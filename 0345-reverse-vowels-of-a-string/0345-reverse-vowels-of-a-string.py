class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')  # Using a set for faster lookup and including uppercase vowels
        s = list(s)  # Convert the string to a list to allow in-place modifications
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]  # Swap the vowels
                left += 1
                right -= 1
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
        
        return ''.join(s)  # Convert the list back to a string

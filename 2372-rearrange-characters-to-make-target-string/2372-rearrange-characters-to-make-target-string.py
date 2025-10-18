class Solution:
    def rearrangeCharacters(self, s, target):
        counter_s = Counter(s)        
        return min(counter_s[c] // count for c,count in Counter(target).items())
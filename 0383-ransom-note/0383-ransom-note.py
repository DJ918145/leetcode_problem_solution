class Solution(object):
    def canConstruct(self, stri1, stri2):
        count1 = {}
        count2 = {}
        for char in stri1:
            if char in count1:
                count1[char] += 1
            else:
                count1[char] = 1
        for char in stri2:
            if char in count2:
                count2[char] += 1
            else:
                count2[char] = 1
        for char in count1:
            if char not in count2 or count1[char] > count2[char]:
                return False
        
        return True
class Solution(object):
    def isAnagram(self, s, t):
        str =[]
        tar = []
        str.extend(s)
        tar.extend(t)
        str.sort()
        tar.sort()
        if str == tar:
            return True
        else:
            return False
        
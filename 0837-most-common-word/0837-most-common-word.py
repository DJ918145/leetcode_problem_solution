class Solution(object):
    def mostCommonWord(self, paragraph, banned):
            paragraph = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph]).split()
            myd = {}
            for i in paragraph:
                if i not in banned:
                    if i in myd:
                        myd[i] +=1
                    else:
                        myd[i] = 1
            return max(myd, key=myd.get)
        
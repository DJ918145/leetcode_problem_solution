class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        a = []
        b = []
        for i in range(1,n+1):
            if i%m!=0:
                a.append(i)
            else:
                b.append(i)
        print(sum(a), sum(b))
        return sum(a)- sum(b)
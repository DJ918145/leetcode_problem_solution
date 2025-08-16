class Solution(object):
    def longestOnes(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k>=arr.count(0):
            return len(arr)
        if k==0:
            maxi = 0
            p = 0
            for i in arr:
                if i == 1:
                    p = p + 1
                else:
                    maxi = max(maxi, p)
                    p = 0
                maxi = max(maxi, p)
                
            return maxi

        l= 0
        r= 0
        maxi = 0
        flipped =0
        for i in range(len(arr)):
            # print(arr[i], l, r, maxi, flipped)
            if arr[i] == 0 and flipped < k:
                l = l+1
                flipped = flipped + 1
            elif arr[i] == 0 and flipped >= k:
                for j in range(r, i):
                    if arr[j] == 0:
                        r = j+1
                        flipped = flipped + 1
                        break
                l = l+1
                maxi = max(maxi, l-r)
            else:
                l = l+1
                maxi = max(maxi, l-r)  
        return maxi
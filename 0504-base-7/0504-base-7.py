class Solution(object):
    def convertToBase7(self, num):
        ans = ""
        i = num
        if num == 0:
            return "0"
        while num != 0:

            if num < 0:
                num = abs(num)

            n = num%7
            ans += str(n)
            num = num//7

        ans = ans[::-1]
            
        if i > 0:
            return ans 
        else:
            return str(-1*int(ans))
        
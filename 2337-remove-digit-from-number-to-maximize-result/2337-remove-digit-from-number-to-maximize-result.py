class Solution(object):
    def removeDigit(self, number, digit):
        output = []
        for i in range(len(number)):
            if number[i] == digit:
                output.append(number[:i]+number[i+1:])
        return max(output)
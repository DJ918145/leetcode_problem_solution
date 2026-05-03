class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        for i in range(len(goal)):
            match = True
            for j in range(len(s)):
                if goal[(i + j) % len(s)] != s[j]:
                    match = False
                    break
            if match:
                return True

        return False

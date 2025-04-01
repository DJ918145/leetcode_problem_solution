class Solution(object):
    def isSubsequence(self, s, t):
        s_idx, t_idx = 0, 0
        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1
        # If we reached the end of `s`, all characters are matched
        return s_idx == len(s)


        
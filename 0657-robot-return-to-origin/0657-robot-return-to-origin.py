class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        curr = [0, 0]
        for move in moves:
            if move=="R":
                curr[0]+=1
            elif move=="L":
                curr[0]-=1
            elif move=="U":
                curr[1]+=1
            else:
                curr[1]-=1
        return True if curr == [0,0] else False
        
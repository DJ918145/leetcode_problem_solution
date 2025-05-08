class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        row = len(moveTime)
        col = len(moveTime[0])
        q = [(0,0,0,1)]
        heapq.heapify(q)
        v = set((0,0))  
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        while q :
            curr_time , x, y,i  = heapq.heappop(q)
            if x == row-1 and y==col-1 :
                return curr_time
            for dx,dy in direction :
                nx,ny  = x + dx , y + dy
                if 0<= nx < row and 0<= ny < col and (nx,ny) not in v :
                    
                    next_time = max(curr_time,moveTime[nx][ny])+i
                    #curr_time += index[i]  # two move
                    #i = (i+1)%2
                    heapq.heappush(q,(next_time,nx,ny,3-i))
                    v.add((nx,ny))
        
        return -1
        
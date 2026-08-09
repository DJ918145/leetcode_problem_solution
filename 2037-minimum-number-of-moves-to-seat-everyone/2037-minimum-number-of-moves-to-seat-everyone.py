class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        
        student_movement = 0
        
        for i in range(len(seats)):
            student_movement += abs(seats[i] - students[i])
            
        return student_movement

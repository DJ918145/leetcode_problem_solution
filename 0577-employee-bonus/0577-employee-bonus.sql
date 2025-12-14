# Write your MySQL query statement below
select Employee.name, Bonus.bonus
From Employee 
Left JOIN Bonus
ON Employee.empID = Bonus.empId 
Where bonus < 1000 OR bonus IS NULL;
# Write your MySQL query statement below
SELECT e_uni.unique_id, e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS e_uni ON e.id = e_uni.id;
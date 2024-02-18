# Write your MySQL query statement below
SELECT Weather1.id
FROM Weather AS Weather1, Weather AS Weather2
WHERE DATEDIFF(Weather1.recordDate, Weather2.recordDate) = 1 AND Weather1.temperature > Weather2.temperature;
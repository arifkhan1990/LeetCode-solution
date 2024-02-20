# Write your MySQL query statement below
SELECT
    project_id,
    IFNULL(ROUND(AVG(E.experience_years), 2), 0) AS average_years
FROM
    Project AS P
LEFT JOIN
    Employee AS E ON P.employee_id = E.employee_id
GROUP BY project_id;
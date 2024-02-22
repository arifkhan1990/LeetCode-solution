# Write your MySQL query statement below
SELECT
    e.employee_id,
    e.name,
    COUNT(sub.employee_id) AS reports_count,
    ROUND(AVG(sub.age)) AS average_age
FROM
    Employees AS e
LEFT JOIN
    Employees AS sub ON e.employee_id = sub.reports_to
GROUP BY
    e.employee_id, e.name
HAVING
    reports_count >= 1
ORDER BY
    employee_id;
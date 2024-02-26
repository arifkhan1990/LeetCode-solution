# Write your MySQL query statement below
SELECT Department, Employee, Salary
FROM (
    SELECT
        D.name AS Department,
        E.name AS Employee,
        E.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY D.name ORDER BY salary DESC) AS salary_rank
    FROM Employee E
    JOIN Department D
    ON E.departmentId = D.id
) AS rank_Table
WHERE
    salary_rank <= 3;

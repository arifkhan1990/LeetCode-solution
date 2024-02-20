# Write your MySQL query statement below
SELECT
    contest_id,
    ROUND(COUNT(R.user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2)
    AS percentage
FROM
    Register R
GROUP BY
    contest_id
ORDER BY
    percentage DESC, 
    contest_id;

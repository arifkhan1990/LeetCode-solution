# Write your MySQL query statement below
SELECT Signups.user_id,
    COALESCE(
        ROUND(
            SUM(CASE WHEN Confirmations.action='confirmed' THEN 1 ELSE 0 END)
            /
            NULLIF(COUNT(Confirmations.user_id), 0)
    , 2), 0) AS confirmation_rate
    FROM Signups
    LEFT JOIN Confirmations ON Signups.user_id = Confirmations.user_id
    GROUP BY Signups.user_id;
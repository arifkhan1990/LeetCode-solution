SELECT user_id AS id, COUNT(*) AS num
FROM (
    SELECT requester_id AS user_id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS user_id
    FROM RequestAccepted
) AS all_users
GROUP BY user_id
ORDER BY num DESC
LIMIT 1;

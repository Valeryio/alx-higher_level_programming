-- grouping in SQL
SELECT score, SUM(score) AS number
FROM second_table
ORDER BY number DESC

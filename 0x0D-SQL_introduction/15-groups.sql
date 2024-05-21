-- grouping in SQL
SELECT score, SUM(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC

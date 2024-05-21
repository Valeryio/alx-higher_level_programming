-- grouping in SQL
SELECT score, COUNT(score) AS number
FROM second_table
ORDER BY number DESC

-- rating genres

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_show_ratings
INNER JOIN tv_genres ON tv_show_ratings.show_id = tv_genres.id
GROUP BY name
ORDER BY rating DESC;


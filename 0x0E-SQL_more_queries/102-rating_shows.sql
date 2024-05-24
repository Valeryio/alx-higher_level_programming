-- rating shows:x

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating FROM tv_show_ratings INNER JOIN tv_shows ON tv_show_ratings.show_id = tv_shows.id GROUP BY title ORDER BY rating DESC;


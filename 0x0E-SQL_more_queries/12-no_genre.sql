-- left join

SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_show_genres
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE genre_id = NULL
ORDER BY title, genre_id;

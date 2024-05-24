-- showing by join

SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_show_genres
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY title, genre_id;

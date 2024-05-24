-- lists all comedy shows contained in hbtn_0d_tvshows
SELECT tv_shows.title AS 'title'
FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;

-- lists all comedy shows contained in hbtn_0d_tvshows
SELECT tv_shows.title AS 'name'
FROM tv_genres
JOIN tv_show_genres
JOIN tv_shows
WHERE tv_genres.name = 'Comedy'
AND tv_genres.id = tv_show_genres.genre_id
AND tv_shows.id = tv_show_genres.show_id
ORDER BY title ASC;

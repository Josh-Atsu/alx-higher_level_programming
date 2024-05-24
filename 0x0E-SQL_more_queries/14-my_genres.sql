-- lists all shows contained in hbtn_0d_tvshows
-- lists all genres of the show Dexter
SELECT tv_genres.name AS 'name'
FROM tv_genres
JOIN tv_show_genres
JOIN tv_shows
WHERE tv_shows.title = 'Dexter'
AND tv_genres.id = tv_show_genres.genre_id
AND tv_shows.id = tv_show_genres.show_id
ORDER BY name ASC;

-- SQL Query
SELECT tv.shows_title, tv.show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv.shows.id = tv_show_genres.show_id
ORDER BY tv.shows_title, tv.show_genres.genre_id ASC;
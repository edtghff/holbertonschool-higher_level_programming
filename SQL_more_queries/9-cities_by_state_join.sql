-- SQL Query
SELECT id, name
FROM cities
JOIN states ON cities.state_id = states.id
SELECT cities.id, cities.name, states.name
ORDER BY cities.id ASC;
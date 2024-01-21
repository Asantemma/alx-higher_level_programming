-- A script lists all cities contained in the database hbtn_0d_usa.

SELECT cities.id, cities.name, states.name
FROM cities c
JOIN states
ON c.state_id = states.id;
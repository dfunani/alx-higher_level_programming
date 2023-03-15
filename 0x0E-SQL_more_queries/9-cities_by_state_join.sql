-- join tables
SELECT cities.id, cities.name, states.name
  FROM cities AS cities
       INNER JOIN states AS states
       ON cities.state_id = states.id
 ORDER BY cities.id;

-- join tables
SELECT cities.id, cities.name, states.name
  FROM hbtn_0d_usa.cities AS cities
       INNER JOIN hbtn_0d_usa.states AS states
       ON cities.state_id = states.id
 ORDER BY cities.id;

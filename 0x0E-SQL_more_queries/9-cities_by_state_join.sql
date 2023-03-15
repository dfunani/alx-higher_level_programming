-- join tables
SELECT id, name, state.name
  FROM cities
       INNER JOIN states AS state
       ON state_id = state.id
 ORDER BY id;

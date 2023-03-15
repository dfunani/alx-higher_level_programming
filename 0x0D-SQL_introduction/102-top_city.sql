-- Top 3
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 or month = 8
GROUP city
ORDER BY avg_temp DESC
LIMIT 3;

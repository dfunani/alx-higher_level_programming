-- Average
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP city
ORDER BY avg_temp DESC;

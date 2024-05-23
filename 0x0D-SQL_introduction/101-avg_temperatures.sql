-- Displays the temperature (in Fahrenheit)
-- city ordered by descending values.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;

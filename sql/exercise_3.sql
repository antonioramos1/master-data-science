SELECT nb_engines, COUNT(nb_engines) AS most_common_engine
FROM optd_aircraft 
WHERE nb_engines IS NOT NULL
GROUP BY nb_engines
ORDER BY most_common_engine DESC
LIMIT 1;


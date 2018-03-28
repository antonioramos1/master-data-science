\! createdb airlines;
\! csvsql -d '^' /home/dsc/Data/opentraveldata/optd_airlines.csv | psql airlines;
\c airlines;
\COPY optd_airlines FROM '/home/dsc/Data/opentraveldata/optd_airlines.csv' DELIMITER '^' CSV HEADER;

\! csvsql -d '^' /home/dsc/Data/opentraveldata/ref_airline_nb_of_flights.csv | psql airlines;
\COPY ref_airline_nb_of_flights FROM '/home/dsc/Data/opentraveldata/ref_airline_nb_of_flights.csv' DELIMITER '^' CSV HEADER;

SELECT ref.*, air.name                            
FROM ref_airline_nb_of_flights ref 
LEFT JOIN optd_airlines air
ON ref.airline_code_2c = air."2char_code";


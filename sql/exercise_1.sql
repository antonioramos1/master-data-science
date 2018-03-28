\! createdb aircraft;
\! csvsql -d '^' /home/dsc/Data/opentraveldata/optd_aircraft.csv | psql aircraft;
\c aircraft;
\COPY optd_aircraft FROM '/home/dsc/Data/opentraveldata/optd_aircraft.csv' DELIMITER '^' CSV HEADER;

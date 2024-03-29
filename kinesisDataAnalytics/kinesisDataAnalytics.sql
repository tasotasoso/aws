CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (AVGTIME TIMESTAMP, AVGTEMPERATURE FLOAT, AVGHUMIDITY FLOAT);

CREATE OR REPLACE  PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"
SELECT STREAM STEP(s.ROWTIME BY INTERVAL '15' SECOND) AS AVGTIME,
              AVG(s.temperature) AS AVGTEMPERATURE,
              AVG(s.humidity) AS AVGHUMIDITY
FROM "SOURCE_SQL_STREAM_001" AS s
-- Uses a 15-second tumbling time window
GROUP BY STEP(s.ROWTIME BY INTERVAL '15' SECOND);
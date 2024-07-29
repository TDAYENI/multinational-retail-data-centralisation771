-- Sales would like the get an accurate metric for how quickly the company is making sales.
-- Determine the average time taken between each sale grouped by year, the 

WITH TimeDiff AS (
  SELECT
    d.year AS year,
    LEAD(d.datetime) OVER (PARTITION BY d.year ORDER BY d.datetime ASC) - d.datetime AS time_diff
  FROM
    dim_date_times d
)

SELECT
  year,
  CONCAT(
    '{"hours": ', FLOOR(AVG(EXTRACT(EPOCH FROM td.time_diff)) / 3600),
    ', "minutes": ', FLOOR(MOD(CAST(AVG(EXTRACT(EPOCH FROM td.time_diff)) AS NUMERIC), 3600) / 60),
    ', "seconds": ', FLOOR(MOD(CAST(AVG(EXTRACT(EPOCH FROM td.time_diff)) AS NUMERIC), 60)),
    ', "milliseconds": ', ROUND(MOD(CAST(AVG(EXTRACT(EPOCH FROM td.time_diff)) AS NUMERIC), 1) * 1000),
    ' }'
  ) AS avg_duration,
  AVG(EXTRACT(EPOCH FROM td.time_diff)) AS avg_duration_seconds
FROM
  TimeDiff td
GROUP BY
  year
ORDER BY
  avg_duration_seconds DESC;

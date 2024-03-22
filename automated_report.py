import snowflake.connector
from datetime import date
from config import SNOWFLAKE_CONFIG

# Defining SQL queries with descriptions
queries = [
    ("Average Temperature for the Day", "SELECT AVG(temperature) AS avg_temperature FROM temperature_data WHERE date = current_date;"),
    ("Maximum Temperature for the Day", "SELECT MAX(temperature) AS max_temperature FROM temperature_data WHERE date = current_date;"),
    ("Minimum Temperature for the Day", "SELECT MIN(temperature) AS min_temperature FROM temperature_data WHERE date = current_date;"),
    ("Hourly Average Temperatures", "SELECT HOUR(timestamp) AS hour, AVG(temperature) AS avg_temperature FROM temperature_data WHERE date = current_date GROUP BY HOUR(timestamp) ORDER BY hour;"),
    ("Temperature Range for Each Hour", "SELECT HOUR(timestamp) AS hour, MIN(temperature) AS min_temperature, MAX(temperature) AS max_temperature FROM temperature_data WHERE date = current_date GROUP BY HOUR(timestamp) ORDER BY hour;"),
    ("Total Number of Measurements per Hour", "SELECT HOUR(timestamp) AS hour, COUNT(*) AS measurement_count FROM temperature_data WHERE date = current_date GROUP BY HOUR(timestamp) ORDER BY hour;"),
    ("Percentage of Time Spent in Each Temperature Range", "SELECT CASE WHEN temperature < 0 THEN 'Below Freezing' WHEN temperature >= 0 AND temperature < 10 THEN '0-10°C' WHEN temperature >= 10 AND temperature < 20 THEN '10-20°C' WHEN temperature >= 20 AND temperature < 30 THEN '20-30°C' ELSE 'Above 30°C' END AS temperature_range, COUNT(*) AS measurement_count, (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM temperature_data WHERE date = current_date)) AS percentage FROM temperature_data WHERE date = current_date GROUP BY temperature_range;")
]

# Connect to Snowflake
conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)

# Get today's date
current_date = date.today().strftime("%Y-%m-%d")

# Execute queries and format results
result_lines = []
for query_description, query in queries:
    cursor = conn.cursor()
    cursor.execute(query.replace('current_date', f"'{current_date}'"))
    result = cursor.fetchone()
    result_lines.append(f"{query_description}: {result[0]}")
    cursor.close()

# Close connection
conn.close()

# Write results to a file
output_file_path = "temperature_analysis.txt"
with open(output_file_path, "w") as f:
    f.write("\n".join(result_lines))

print(f"Results written to {output_file_path}")s

import duckdb
import os

# Ensure directory exists
os.makedirs("evidence/sources/demo", exist_ok=True)

# Create mock data and export to CSV
con = duckdb.connect()
con.sql("CREATE TABLE test_table AS SELECT 1 as id, 'Hello World' as message, 100 as value UNION ALL SELECT 2, 'Evidence is Cool', 200")
csv_path = "evidence/sources/demo/test_table.csv"
con.sql(f"COPY test_table TO '{csv_path}' (HEADER, DELIMITER ',')")

print(f"Created demo CSV at {csv_path}")
con.close()

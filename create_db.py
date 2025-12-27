import duckdb
import os

# Ensure directory exists
os.makedirs("evidence/sources/demo", exist_ok=True)

# Create database and table
db_path = "evidence/sources/demo/demo.duckdb"
con = duckdb.connect(db_path)
con.sql("CREATE TABLE IF NOT EXISTS test_table AS SELECT 1 as id, 'Hello World' as message, 100 as value UNION ALL SELECT 2, 'Evidence is Cool', 200")
print(f"Created demo database at {db_path}")
print(con.sql("SELECT * FROM test_table").fetchall())
con.close()

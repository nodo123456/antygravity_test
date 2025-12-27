import duckdb
import os
from generation.generators import generate_events_df

def create_database():
    # 1. Setup
    os.makedirs("database", exist_ok=True)
    db_path = "database/raw.duckdb"
    
    # 2. Get Data
    df = generate_events_df(1000)
    
    # 3. Load to DuckDB using SQL file
    con = duckdb.connect(db_path)
    
    # Register DataFrame as a view so SQL can see it
    con.register('df_view', df)
    
    # Read and Execute DDL
    with open("generation/schema/raw_events.sql", "r") as f:
        sql = f.read()
        con.sql(sql)
    
    print(f"Data saved to {db_path}")
    print(con.sql("SELECT event_type, count(*) as count FROM raw_events GROUP BY 1 ORDER BY 2 DESC").fetchall())
    con.close()

if __name__ == "__main__":
    create_database()

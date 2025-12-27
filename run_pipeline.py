import os
import subprocess
import duckdb

def run_pipeline():
    # 1. Generate Data
    print("--- 1. Generating Data ---")
    subprocess.run(["python", "create_db.py"], check=True)
    
    # 2. Run dbt
    print("--- 2. Running dbt ---")
    subprocess.run(["dbt", "build", "--project-dir", "dbt", "--profiles-dir", "dbt"], check=True)
    
    # 3. Export to Evidence
    print("--- 3. Exporting to Evidence ---")
    con = duckdb.connect("database/raw.duckdb")
    
    # Debug: List tables
    print("DuckDB Tables found:", con.sql("SHOW TABLES").fetchall())
    
    output_dir = "evidence/sources/synthetic"
    os.makedirs(output_dir, exist_ok=True)
    
    # Export daily_stats
    print("Exporting daily_stats.csv...")
    # Explicitly check if table exists to avoid confusing error
    try:
        con.sql(f"COPY (SELECT * FROM daily_stats) TO '{output_dir}/daily_stats.csv' (HEADER, DELIMITER ',')")
        print("Export daily_stats successful.")
        
        con.sql(f"COPY (SELECT * FROM stg_customers LIMIT 100) TO '{output_dir}/customers.csv' (HEADER, DELIMITER ',')")
        print("Export customers successful.")
    except Exception as e:
        print(f"Export FAILED: {e}")
        # List tables again to be sure
        print("Tables available:", con.sql("SHOW TABLES").fetchall())
        raise e
    
    con.close()
    print("--- Pipeline Complete ---")

if __name__ == "__main__":
    run_pipeline()

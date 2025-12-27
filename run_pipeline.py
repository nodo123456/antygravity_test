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
    con = duckdb.connect("ingestion/raw.duckdb")
    
    output_dir = "evidence/sources/synthetic"
    os.makedirs(output_dir, exist_ok=True)
    
    # Export daily_stats
    print("Exporting daily_stats.csv...")
    con.sql(f"COPY (SELECT * FROM daily_stats) TO '{output_dir}/daily_stats.csv' (HEADER, DELIMITER ',')")
    
    con.close()
    print("--- Pipeline Complete ---")

if __name__ == "__main__":
    run_pipeline()

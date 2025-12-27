import duckdb
import os

def export_data():
    conn = duckdb.connect("mds_box.duckdb")
    
    # Ensure directory exists
    os.makedirs("evidence/sources/my_project", exist_ok=True)
    
    # Export dim_commits to CSV
    # We use timestamps in filename or just overwrite to keep it simple for Evidence
    conn.sql("COPY (SELECT * FROM dim_commits) TO 'evidence/sources/my_project/dim_commits.csv' (HEADER, DELIMITER ',')")
    
    print("Exported dim_commits.csv")
    conn.close()

if __name__ == "__main__":
    export_data()

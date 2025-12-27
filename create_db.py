import duckdb
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

def generate_data():
    print("Generating 1000 rows of synthetic data...")
    
    # 1. Setup
    num_rows = 1000
    os.makedirs("ingestion", exist_ok=True)
    db_path = "ingestion/raw.duckdb"
    
    # 2. Generate Random Data
    # Dates: Last 30 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    dates = [start_date + timedelta(seconds=random.randint(0, 30*24*3600)) for _ in range(num_rows)]
    
    # Event Types
    events = ['login', 'view_item', 'add_to_cart', 'purchase', 'log_error']
    weights = [0.4, 0.3, 0.15, 0.1, 0.05]
    event_types = random.choices(events, weights=weights, k=num_rows)
    
    # Users
    user_ids = [random.randint(1001, 1100) for _ in range(num_rows)] # 100 users
    
    # Values (revenue for purchase, 0 otherwise)
    values = []
    for et in event_types:
        if et == 'purchase':
            values.append(round(random.uniform(9.99, 199.99), 2))
        else:
            values.append(0.0)
            
    df = pd.DataFrame({
        'event_id': range(1, num_rows + 1),
        'timestamp': dates,
        'user_id': user_ids,
        'event_type': event_types,
        'value': values
    })
    
    # 3. Load to DuckDB
    con = duckdb.connect(db_path)
    con.sql("CREATE OR REPLACE TABLE raw_events AS SELECT * FROM df")
    
    print(f"Data saved to {db_path}")
    print(con.sql("SELECT event_type, count(*) as count FROM raw_events GROUP BY 1 ORDER BY 2 DESC").fetchall())
    con.close()

if __name__ == "__main__":
    generate_data()

import duckdb
import os
import importlib.util
import sys

# Define domains to process
DOMAINS = ['events', 'customers']

def create_database():
    # 1. Setup
    os.makedirs("database", exist_ok=True)
    db_path = "database/raw.duckdb"
    con = duckdb.connect(db_path)
    
    for domain in DOMAINS:
        print(f"--- Processing Domain: {domain} ---")
        
        # Load Generator Module dynamically
        # (Or simpler: just import them if structure is known, but dynamic is nice for extensibility)
        # For simplicity/robustness, let's just do direct imports or standard import logic
        # Actually, standard import is cleaner given the structure
        module_name = f"generation.{domain}.generator"
        
        # Import module
        try:
             mod = __import__(module_name, fromlist=['generate'])
             df = mod.generate()
             
             # Register as view
             con.register('df_view', df)
             
             # Execute Schema
             schema_path = f"generation/{domain}/schema.sql"
             with open(schema_path, 'r') as f:
                 sql = f.read()
                 con.sql(sql)
                 
             print(f"Created table for {domain}")
             
        except ImportError as e:
            print(f"Error loading generator for {domain}: {e}")
        except Exception as e:
            print(f"Error processing {domain}: {e}")

    # Verify
    print("\n--- Database Stats ---")
    print("Tables:", con.sql("SHOW TABLES").fetchall())
    con.close()

if __name__ == "__main__":
    create_database()

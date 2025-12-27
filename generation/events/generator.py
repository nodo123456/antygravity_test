import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate(num_rows=1000):
    print(f"Generating {num_rows} rows of synthetic events...")
    
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
    
    return df
